import sqlite3

DB_NAME = "project.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        text TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def save_score(name, score):
    #try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))

        conn.commit()
        conn.close()


def load_scores():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name, score FROM scores")
    rows = cursor.fetchall()

    conn.close()
    return rows

def save_log(text):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO logs (text) VALUES (?)",
        (text,)
    )

    conn.commit()
    conn.close()

def load_logs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT timestamp, text FROM logs  ORDER BY id DESC"
    )
    rows = cursor.fetchall()

    conn.close()
    return rows