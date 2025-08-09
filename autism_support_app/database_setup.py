import sqlite3

def init_db():
    conn = sqlite3.connect('autism_users.db')
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    email TEXT UNIQUE,
    password_hash BLOB,
    mobile TEXT,
    parent_type TEXT,
    child_age INTEGER,
    condition TEXT,
    therapy TEXT,
    language TEXT
    )
    """)
    conn.commit()
    conn.close()
    print("Database initialized.")

if __name__ == "__main__":
    init_db()
