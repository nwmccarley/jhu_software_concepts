import psycopg2.pool
import json
from datetime import datetime

# PostgreSQL connection
DATABASE_URL = "postgresql://neondb_owner:npg_PhLQBRjM7Cb3@ep-withered-hall-a5aocygy.us-east-2.aws.neon.tech/neondb?sslmode=require"

# Set up connection pool
pool = psycopg2.pool.SimpleConnectionPool(0, 80, DATABASE_URL)
conn = pool.getconn()
cur = conn.cursor()

# Step 1: Create table with 'program' as combined university + program
cur.execute("""
    CREATE TABLE IF NOT EXISTS applicants (
        id SERIAL PRIMARY KEY,
        program TEXT,
        degree TEXT,
        date_added DATE,
        applicant_status TEXT,
        start_date TEXT,
        gre FLOAT,
        gre_v FLOAT,
        gre_aw FLOAT,
        gpa FLOAT,
        applicant_type TEXT,
        comments TEXT,
        url_link TEXT
    );
""")

# Step 2: Load JSON
with open("applicant_data.json", "r") as f:
    data = json.load(f)

# Step 3: Helpers
def parse_float(value):
    try:
        return float(value)
    except:
        return None

def parse_date(value):
    try:
        return datetime.strptime(value, "%b %d, %Y").date()
    except:
        try:
            return datetime.strptime(value, "%B %d, %Y").date()
        except:
            return None

# Step 4: Prepare insert
insert_query = """
    INSERT INTO applicants (
        program, degree, date_added, applicant_status,
        start_date, gre, gre_v, gre_aw, gpa, applicant_type,
        comments, url_link
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

values = []
for row in data:
    university = row.get("University", "").strip()
    program = row.get("Program", "").strip()
    program_combined = f"{university} - {program}" if university or program else None

    values.append((
        program_combined,
        row.get("Degree"),
        parse_date(row.get("Date Information Added to Grad Cafe")),
        row.get("Applicant Status"),
        row.get("Start Date"),
        parse_float(row.get("GRE")),
        parse_float(row.get("GRE V")),
        parse_float(row.get("GRE AW")),
        parse_float(row.get("GPA")),
        row.get("International/American Student"),
        row.get("Comments"),
        row.get("Url link")
    ))

# Step 5: Insert in chunks
chunk_size = 1000
total = len(values)
print(f"Starting insert of {total} applicant records...")

for i in range(0, total, chunk_size):
    chunk = values[i:i + chunk_size]
    cur.executemany(insert_query, chunk)
    conn.commit()
    print(f"Inserted {min(i + chunk_size, total)} of {total} records...")

# Step 6: Close everything
cur.close()
pool.putconn(conn)
pool.closeall()

print("✅ All applicant records inserted with combined 'program'.")
