from db import get_connection

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    print("Initializing DB...")
    init_db()
    print("Done")