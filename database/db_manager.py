import sqlite3

def init_db():
    conn = sqlite3.connect("gym_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL,
            reps INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_exercise(name, weight, reps, date):
    conn = sqlite3.connect("gym_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO exercises (name, weight, reps, date) VALUES (?, ?, ?, ?)",
                   (name, weight, reps, date))
    conn.commit()
    conn.close()

def get_all_exercises():
    conn = sqlite3.connect("gym_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exercises ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
