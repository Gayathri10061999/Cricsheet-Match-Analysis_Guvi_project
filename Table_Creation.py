import sqlite3
#import mysql.connector

conn = sqlite3.connect("cricsheet.db")
cursor = conn.cursor()



cursor.execute("""
CREATE TABLE IF NOT EXISTS t20_matches (
    match_id TEXT PRIMARY KEY,
    date DATE,
    venue TEXT,
    team1 TEXT,
    team2 TEXT,
    winner TEXT,
    match_type TEXT
);

""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS deliveries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id TEXT,
    batting_team TEXT,
    batter TEXT,
    bowler TEXT,
    runs INTEGER,
    extras INTEGER,
    FOREIGN KEY(match_id) REFERENCES t20_matches(match_id)
);
""")
conn.commit()
print("commit succeded")
conn.close()
