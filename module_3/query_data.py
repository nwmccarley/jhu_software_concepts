import psycopg2

DATABASE_URL = "postgresql://neondb_owner:npg_PhLQBRjM7Cb3@ep-withered-hall-a5aocygy.us-east-2.aws.neon.tech/neondb?sslmode=require"

def get_all_query_results():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # Question 1 query
    cur.execute("SELECT COUNT(*) FROM applicants WHERE TRIM(term) = 'Fall 2025';")
    q1 = cur.fetchone()[0]

    # Question 2 query
    cur.execute("SELECT COUNT(*) FROM applicants;")
    total = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM applicants WHERE LOWER(us_or_international) = 'international';")
    intl = cur.fetchone()[0]
    q2 = round((intl / total) * 100, 2) if total else 0

    # Question 3 query
    cur.execute("""
        SELECT
          ROUND(AVG(gpa)::numeric, 2),
          ROUND(AVG(gre)::numeric, 2),
          ROUND(AVG(gre_v)::numeric, 2),
          ROUND(AVG(gre_aw)::numeric, 2)
        FROM applicants;
    """)
    q3 = cur.fetchone()

    # Question 4 query
    cur.execute("""
        SELECT ROUND(AVG(gpa)::numeric, 2)
        FROM applicants
        WHERE TRIM(term) = 'Fall 2025'
            AND LOWER(us_or_international) = 'american';
    """)
    gpas = [float(row[0]) for row in cur.fetchall()]
    q4 = round(sum(gpas) / len(gpas), 2) if gpas else "N/A"

    # Question 5 query
    cur.execute("SELECT COUNT(*) FROM applicants WHERE TRIM(term) = 'Fall 2025';")
    total_fall = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM applicants WHERE TRIM(term) = 'Fall 2025' AND LOWER(status) LIKE '%accepted%';")
    accepted = cur.fetchone()[0]
    q5 = round((accepted / total_fall) * 100, 2) if total_fall else "N/A"

    # Question 6 query
    cur.execute("""
        SELECT ROUND(AVG(gpa)::numeric, 2)
        FROM applicants
        WHERE TRIM(term) = 'Fall 2025'
          AND LOWER(status) LIKE '%accepted%';
    """)
    q6 = cur.fetchone()[0] or "N/A"

    # Question 7 query
    cur.execute("""
        SELECT COUNT(*) FROM applicants
        WHERE LOWER(program) LIKE 'johns hopkins university%computer science%'
          AND LOWER(degree) = 'masters';
    """)
    q7 = cur.fetchone()[0]

    cur.close()
    conn.close()

    return {
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "q4": q4,
        "q5": q5,
        "q6": q6,
        "q7": q7
    }

# Output with answers to the terminal
if __name__ == "__main__":
    results = get_all_query_results()

    print("1. How many entries do you have in your database who have applied for Fall 2025?")
    print(f"Answer: {results['q1']} applicants applied for Fall 2025.\n")

    print("2. What percentage of entries are from international students (not American or Other)?")
    print(f"Answer: {results['q2']}%\n")

    print("3. What is the average GPA, GRE, GRE V, GRE AW of applicants who provide these metrics?")
    print(f"Answer:\nAverage GPA: {results['q3'][0]}\nAverage GRE: {results['q3'][1]}\nAverage GRE V: {results['q3'][2]}\nAverage GRE AW: {results['q3'][3]}\n")

    print("4. What is the average GPA of American students in Fall 2025?")
    print(f"Answer: {results['q4']}\n")

    print("5. What percent of entries for Fall 2025 are Acceptances (to two decimal places)?")
    print(f"Answer: {results['q5']}%\n")

    print("6. What is the average GPA of applicants who applied for Fall 2025 and were accepted?")
    print(f"Answer: {results['q6']}\n")

    print("7. How many entries are from applicants who applied to Johns Hopkins University for a master's degree in Computer Science?")
    print(f"Answer: {results['q7']}")
