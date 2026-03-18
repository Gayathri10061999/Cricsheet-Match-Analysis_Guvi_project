import sqlite3
conn = sqlite3.connect("cricsheet.db")
cursor = conn.cursor()

# 1. View all matches 
cursor.execute(""" SELECT * FROM processed_matches;
""")

# 2. View all deliveries 
cursor.execute(""" SELECT * FROM processed_deliveries;
""")

# 3. Count total matches 
cursor.execute(""" SELECT COUNT(*) AS total_matches FROM
processed_matches;
""")

# 4. Count total deliveries 
cursor.execute(""" SELECT COUNT(*) AS total_deliveries FROM
processed_deliveries;
""")

# 5. Total runs scored by each batter 
cursor.execute(""" SELECT batter, SUM(runs) AS
total_runs FROM processed_deliveries GROUP BY batter ORDER BY total_runs
DESC;
""")

# 6. Top 10 batters 
cursor.execute(""" SELECT batter, SUM(runs) AS total_runs FROM
processed_deliveries GROUP BY batter ORDER BY total_runs DESC LIMIT 10;
""")

# 7. Total runs per match 
cursor.execute(""" SELECT match_id, SUM(runs) AS match_runs FROM
processed_deliveries GROUP BY match_id;
""")

# 8. Average runs per batter 
cursor.execute(""" SELECT batter, AVG(runs) AS avg_runs FROM
processed_deliveries GROUP BY batter;
""")

# 9. Total runs conceded by each bowler 
cursor.execute(""" SELECT bowler, SUM(runs +
extras) AS runs_conceded FROM processed_deliveries GROUP BY bowler ORDER
BY runs_conceded ASC;
""")

# 10. Total runs scored by each team 
cursor.execute(""" SELECT batting_team, SUM(runs) AS
total_runs FROM processed_deliveries GROUP BY batting_team ORDER BY
total_runs DESC;
""")

# 11. Number of matches won by each team 
cursor.execute(""" SELECT winner, COUNT(*) AS wins
FROM processed_matches GROUP BY winner ORDER BY wins DESC;
""")

# 12. Latest match played 
cursor.execute(""" SELECT * FROM processed_matches ORDER BY date
DESC LIMIT 1;
""")

# 13. Matches played at each venue 
cursor.execute(""" SELECT venue, COUNT(*) AS match_count
FROM processed_matches GROUP BY venue ORDER BY match_count DESC;
""")

# 14. Total runs in each match with venue 
cursor.execute(""" SELECT m.match_id, m.venue,
SUM(d.runs) AS total_runs FROM processed_matches m JOIN
processed_deliveries d ON m.match_id = d.match_id GROUP BY m.match_id,
m.venue;
""")

# 15. Top scorer in each match 
cursor.execute(""" SELECT d.match_id, d.batter, SUM(d.runs)
AS runs FROM processed_deliveries d GROUP BY d.match_id, d.batter ORDER
BY d.match_id, runs DESC;
""")

# 16. Highest scoring match 
cursor.execute(""" SELECT match_id, SUM(runs) AS total_runs
FROM processed_deliveries GROUP BY match_id ORDER BY total_runs DESC
LIMIT 1;
""")

# 17. Player with most matches played 
cursor.execute(""" SELECT batter, COUNT(DISTINCT
match_id) AS matches_played FROM processed_deliveries GROUP BY batter
ORDER BY matches_played DESC;
""")

# 18. Matches won by each team type 
cursor.execute(""" SELECT match_type, winner, COUNT(*)
AS wins FROM processed_matches GROUP BY match_type, winner ORDER BY
match_type, wins DESC;
""")

# 19. Total extras per match 
cursor.execute(""" SELECT match_id, SUM(extras) AS
total_extras FROM processed_deliveries GROUP BY match_id;
""")

# 20. Economy-like metric per bowler 
cursor.execute(""" SELECT bowler, SUM(runs + extras) *
1.0 / COUNT(*) AS avg_runs_per_ball FROM processed_deliveries GROUP BY
bowler ORDER BY avg_runs_per_ball ASC;
""")



tables=cursor.fetchall()

for table in tables:
    print(table)



