import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Load Data
matches = pd.read_csv("C:/Users/gayat/AppData/Local/Programs/Python/Python313/processed_matches.csv")
deliveries = pd.read_csv("C:/Users/gayat/AppData/Local/Programs/Python/Python313/processed_deliveries.csv")



# 1. Top 10 Batters
top_batters = deliveries.groupby("batter")["runs"].sum().nlargest(10)
plt.figure()
top_batters.plot(kind="bar")
plt.title("Top 10 Batters")
plt.xticks(rotation=45)
plt.show()

# 2. Matches per Venue
plt.figure()
sns.countplot(data=matches, x="venue", order=matches["venue"].value_counts().index[:10])
plt.xticks(rotation=90)
plt.title("Matches per Venue")
plt.show()

# 3. Runs Distribution
plt.figure()
sns.histplot(deliveries["runs"], bins=10)
plt.title("Runs Distribution per bowler")
plt.show()

# 4. Matches Over Time
matches["date"] = pd.to_datetime(matches["date"])
matches_per_year = matches.groupby(matches["date"].dt.year).size()
plt.figure()
matches_per_year.plot()
plt.title("Matches Over Years")
plt.show()

# 5. Top Teams by Wins
wins = matches["winner"].value_counts().reset_index()
wins.columns = ["team", "wins"]
fig = px.bar(wins.head(10), x="team", y="wins", title="Top Teams by Wins")
fig.show()

# 6. Runs per Match
runs_per_match = deliveries.groupby("match_id")["runs"].sum()
plt.figure()
runs_per_match.plot(kind="line")
plt.title("Runs per Match")
plt.show()

# 7. Top Economical Bowlers
bowler_stats = deliveries.groupby("balls").agg({
    "runs": "sum",
    "balls": "count"
}).reset_index()
bowler_stats["economy"] = bowler_stats["runs"] / bowler_stats["bowler"]
top_bowlers = bowler_stats.nsmallest(10, "economy")
plt.figure()
sns.barplot(data=top_bowlers, x="bowler", y="economy")
plt.xticks(rotation=45)
plt.title("Top Economical Bowlers")
plt.show()

# 8. Match Type Distribution
fig = px.pie(matches, names="match_type", title="Match Type Distribution")
fig.show()

# 9. Runs by Team
team_runs = deliveries.groupby("batting_team")["runs"].sum().reset_index()
plt.figure()
sns.barplot(data=team_runs, x="batting_team", y="runs")
plt.xticks(rotation=90)
plt.title("Runs by Team")
plt.show()

# 10. Runs per Batter
batter_stats = deliveries.groupby("batter").agg({
    "runs": "sum",
    "bowler": "count"
}).reset_index()
fig = px.scatter(batter_stats, x="bowler", y="runs", title="Runs vs bowlers per Batter")
fig.show()
