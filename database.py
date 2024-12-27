import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS complaints (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    contact TEXT,
                    complaint TEXT
                )
            """)
            conn.commit()

    def save_complaint(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                INSERT INTO complaints (name, contact, complaint)
                VALUES (?, ?, ?)
            """, (data["name"], data["contact"], data["complaint"]))

    def get_all_complaints(self):
        with sqlite3.connect(self.path) as conn:
            conn.row_factory = sqlite3.Row
            result = conn.execute("SELECT * FROM complaints")
            data = result.fetchall()
            return [dict(row) for row in data]
