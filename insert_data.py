import sqlite3
import pandas as pd

conn = sqlite3.connect("cricsheet.db")

matches_df = pd.read_csv("C:/Users/gayat/AppData/Local/Programs/Python/Python313/processed_matches.csv")
deliveries_df = pd.read_csv("C:/Users/gayat/AppData/Local/Programs/Python/Python313/processed_deliveries.csv")

matches_df.to_sql("t20_matches", conn, if_exists="append", index=False)
deliveries_df.to_sql("deliveries", conn, if_exists="append", index=False)

conn.close()
print("Data inserted successfully")
