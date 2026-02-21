import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

matches_df = pd.read_csv("C:/Users/gayat/AppData/Local/Programs/Python/Python313/processed_matches.csv")
deliveries_df = pd.read_csv("C:/Users/gayat/AppData/Local/Programs/Python/Python313/processed_deliveries.csv")

# 1. Top batsmen
top_batsmen = deliveries_df.groupby("batter")["runs"].sum().sort_values(ascending=False).head(10)
top_batsmen.plot(kind="bar", title="Top 10 Batsmen")
plt.show()

# 2. Match type distribution
sns.countplot(x="match_type", data=matches_df)
plt.title("Match Type Distribution")
plt.show()

# 3. Runs distribution
sns.histplot(deliveries_df["runs"], bins=30)
plt.title("Runs Distribution")
plt.show()

# 4. Wickets by bowler
top_bowlers = deliveries_df.groupby("bowler")["wicket"].sum().sort_values(ascending=False).head(10)
top_bowlers.plot(kind="bar", title="Top Bowlers")
plt.show()
