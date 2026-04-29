import sqlite3
from config import DB_NAME

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        work_hours REAL,
        overtime INTEGER,
        emails INTEGER,
        meetings INTEGER,
        tasks INTEGER,
        vacation INTEGER,
        risk_level TEXT,
        risk_percentage TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_prediction(user_id, data, result):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions 
    (user_id, work_hours, overtime, emails, meetings, tasks, vacation, risk_level, risk_percentage)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        data[0], data[1], data[2], data[3], data[4], data[5],
        result["risk_level"],
        result["risk_percentage"]
    ))

    conn.commit()
    conn.close()


def get_user_history(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM predictions WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()

    conn.close()
    return rows