import sqlite3

def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS results (
            name TEXT,
            score REAL,
            missing_skills TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_result(name, score, missing_skills):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO results VALUES (?, ?, ?)",
        (name, score, ", ".join(missing_skills))
    )

    conn.commit()
    conn.close()


def get_ranked_results():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()

    c.execute("SELECT * FROM results ORDER BY score DESC")
    results = c.fetchall()

    conn.close()
    return results