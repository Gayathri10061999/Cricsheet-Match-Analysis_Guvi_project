import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/cleaned/odi_summary.csv")

# Top winning teams
top_winners = df['winner'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_winners.index, y=top_winners.values)
plt.title("Top 10 Winning Teams in ODIs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../docs/eda_top_winners.png")
plt.show()
