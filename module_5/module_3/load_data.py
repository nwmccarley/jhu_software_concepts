"""Script to load applicant data from JSON and insert it into a PostgreSQL database."""

import json
from datetime import datetime
import psycopg2
from psycopg2 import pool, sql

# PostgreSQL connection
DATABASE_URL = (
    "postgresql://neondb_owner:npg_PhLQBRjM7Cb3@ep-withered-hall-a5aocygy.us-east-2."
    "aws.neon.tech/neondb?sslmode=require"
)


def parse_float(value):
    """Convert value to float, return None if conversion fails."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def parse_date(value):
    """Convert date string to datetime.date, return None if parsing fails."""
    try:
        return datetime.strptime(value, "%b %d, %Y").date()
    except (TypeError, ValueError):
        try:
            return datetime.strptime(value, "%B %d, %Y").date()
        except (TypeError, ValueError):
            return None


def load_applicants(file_path):
    """Load and parse applicant data from JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def create_table(cursor):
    """Create applicants table in the database if it does not exist."""
    create_stmt = sql.SQL(
        """
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
        """
    )
    cursor.execute(create_stmt)


def prepare_values(data):
    """Prepare tuple values for database insertion from parsed JSON data."""
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
    return values


def insert_records(cursor, connection, values, chunk_size=1000):
    """Insert values into the applicants table in chunks."""
    insert_stmt = sql.SQL(
        """
        INSERT INTO applicants (
            program, degree, date_added, status,
            term, gre, gre_v, gre_aw, gpa, us_or_international,
            comments, url
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    )
    total = len(values)
    print(f"Starting insert of {total} applicant records...")
    for i in range(0, total, chunk_size):
        chunk = values[i:i + chunk_size]
        cursor.executemany(insert_stmt, chunk)
        connection.commit()
        print(f"Inserted {min(i + chunk_size, total)} of {total} records...")


def main():
    """Main function to orchestrate JSON loading and DB insertion."""
    connection_pool = pool.SimpleConnectionPool(0, 80, DATABASE_URL)
    conn = connection_pool.getconn()
    cur = conn.cursor()

    create_table(cur)

    data = load_applicants("applicant_data.json")
    values = prepare_values(data)
    insert_records(cur, conn, values)

    cur.close()
    connection_pool.putconn(conn)
    connection_pool.closeall()

    print("All applicant records inserted.")


if __name__ == "__main__":
    main()
