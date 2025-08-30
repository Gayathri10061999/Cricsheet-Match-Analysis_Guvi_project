import sqlite3
import pandas as pd

# Connect to SQLite
conn = sqlite3.connect("../database/cricsheet.db")
cursor = conn.cursor()

# Create ODI table
cursor.execute("""
CREATE TABLE IF NOT EXISTS odi_matches (
    match_id TEXT PRIMARY KEY,
    team1 TEXT,
    team2 TEXT,
    venue TEXT,
    date TEXT,
    match_type TEXT,
    winner TEXT
)
""")

# Insert data
df = pd.read_csv("../data/cleaned/odi_summary.csv")
df.to_sql("odi_matches", conn, if_exists="replace", index=False)

conn.commit()
conn.close()
print("Data inserted into database.")
