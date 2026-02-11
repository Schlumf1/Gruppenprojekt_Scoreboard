import sqlite3

DB_NAME = "project.db"

class Database:
    def __init__(self, db_name=DB_NAME):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.init_db()

    def init_db(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            text TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def save_score(self, name, score):
        try:
            self.cursor.execute(
                "INSERT INTO scores (name, score) VALUES (?, ?)",
                (name, score)
            )
            self.conn.commit()
            return True

        except sqlite3.Error as e:
            print(f"Fehler beim speichern des Scores: {e}")
            return False

    def load_scores(self):
        try:
            return self.cursor.execute("SELECT name, score FROM scores").fetchall()
        except sqlite3.Error as e:
            print(f"Fehler beim laden der Scores: {e}")
            return []

    def load_scores_sorted(self):
        try:
            return self.cursor.execute("SELECT name, score FROM scores ORDER BY score DESC").fetchall()
        except sqlite3.Error as e:
            print(f"Fehler beim laden der sortierten Scores: {e}")
            return []

    def load_top_3_scores(self):
        try:
            return self.cursor.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 3").fetchall()
        except sqlite3.Error as e:
            print(f"Fehler beim laden der Top 3 Scores: {e}")
            return []

    def load_high_score(self):
        try:
            return self.cursor.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 1").fetchone()
        except sqlite3.Error as e:
            print(f"Fehler beim laden des Highscores: {e}")
            return None

    def load_average_score(self):
        try:
            result = self.cursor.execute("SELECT AVG(score) FROM scores").fetchone()
            return result[0] if result and result[0] is not None else None
        except sqlite3.Error as e:
            print(f"Fehler beim berechnen des Durchschnitts: {e}")
            return None

    def load_scores_by_player(self, name):
        try:
            return self.cursor.execute(
                "SELECT name, score FROM scores WHERE LOWER(name) = LOWER(?) ORDER BY score DESC",
                (name,)
            ).fetchall()
        except sqlite3.Error as e:
            print(f"Fehler beim laden der Scores von {name}: {e}")
            return []

    def save_log(self, text):
        try:
            self.cursor.execute(
                "INSERT INTO logs (text) VALUES (?)",
                (text,)
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Fehler beim schreiben des Logs: {e}")

    def load_logs(self):
        try:
            return self.cursor.execute(
                "SELECT timestamp, text FROM logs  ORDER BY id DESC"
            ).fetchall()
        except sqlite3.Error as e:
            print(f"Fehler beim laden des Logs: {e}")
            return []

    def close(self):
        self.conn.close()