import psycopg2.pool
import json
from datetime import datetime

# PostgreSQL connection
DATABASE_URL = "postgresql://neondb_owner:npg_PhLQBRjM7Cb3@ep-withered-hall-a5aocygy.us-east-2.aws.neon.tech/neondb?sslmode=require"

# Set up connection pool
pool = psycopg2.pool.SimpleConnectionPool(0, 80, DATABASE_URL)
conn = pool.getconn()
cur = conn.cursor()

# Create a table in SQL with the updated column names
cur.execute("""
    CREATE TABLE IF NOT EXISTS applicants (
        p_id SERIAL PRIMARY KEY,
        program TEXT,
        comments TEXT,
        date_added DATE,
        url TEXT,
        status TEXT,
        term TEXT,
        us_or_international TEXT,
        gpa FLOAT,
        gre FLOAT,
        gre_v FLOAT,
        gre_aw FLOAT,
        degree TEXT
    );
""")

# Load JSON
with open("applicant_data.json", "r") as f:
    data = json.load(f)

# Helpers to return value types required
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

# Prepare insert with required column names
insert_query = """
    INSERT INTO applicants (
        program, degree, date_added, status,
        term, gre, gre_v, gre_aw, gpa, us_or_international,
        comments, url
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Build values for insertion
values = []
for row in data:
    university = row.get("University", "").strip()
    program = row.get("Program", "").strip()
    program_combined = f"{university} - {program}" if university or program else None

    values.append((
        program_combined,  # program
        row.get("Degree"),  # degree
        parse_date(row.get("Date Information Added to Grad Cafe")),  # date_added
        row.get("Applicant Status"),  # status
        row.get("Start Date"),  # term
        parse_float(row.get("GRE")),  # gre
        parse_float(row.get("GRE V")),  # gre_v
        parse_float(row.get("GRE AW")),  # gre_aw
        parse_float(row.get("GPA")),  # gpa
        row.get("International/American Student"),  # us_or_international
        row.get("Comments"),  # comments
        row.get("Url link")  # url
    ))

# Insert in chunks
chunk_size = 1000
total = len(values)
print(f"Starting insert of {total} applicant records...")

for i in range(0, total, chunk_size):
    chunk = values[i:i + chunk_size]
    cur.executemany(insert_query, chunk)
    conn.commit()
    print(f"Inserted {min(i + chunk_size, total)} of {total} records...")

# Close everything
cur.close()
pool.putconn(conn)
pool.closeall()

print("All applicant records inserted.")
