import psycopg

DATABASE_URL = "postgresql://your_user:your_pass@your_host:port/your_db"

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        print(cur.fetchone())
