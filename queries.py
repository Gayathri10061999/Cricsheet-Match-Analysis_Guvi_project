-- 1. Top 10 ODI matches by total runs scored
SELECT match_id, team1, team2, SUM(runs) as total_runs
FROM odi_deliveries
GROUP BY match_id
ORDER BY total_runs DESC
LIMIT 10;

-- 2. Top 10 run scorers in ODI
SELECT batsman, SUM(runs) as total_runs
FROM odi_deliveries
GROUP BY batsman
ORDER BY total_runs DESC
LIMIT 10;

-- 3. Team with highest ODI win percentage
SELECT winner, COUNT(*) as wins
FROM odi_matches
GROUP BY winner
ORDER BY wins DESC;
