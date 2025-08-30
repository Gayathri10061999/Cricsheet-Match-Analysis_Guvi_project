import os
import json
import pandas as pd

RAW_DATA_PATH = "../data/raw_json/odi"
all_matches = []

for filename in os.listdir(RAW_DATA_PATH):
    if filename.endswith(".json"):
        with open(os.path.join(RAW_DATA_PATH, filename), "r") as file:
            data = json.load(file)

            match_info = {
                "match_id": filename.replace(".json", ""),
                "team1": data["info"]["teams"][0],
                "team2": data["info"]["teams"][1],
                "venue": data["info"].get("venue", None),
                "date": data["info"]["dates"][0],
                "match_type": data["info"].get("match_type", None),
                "winner": data["info"].get("outcome", {}).get("winner", None),
            }
            all_matches.append(match_info)

df = pd.DataFrame(all_matches)
df.to_csv("../data/cleaned/odi_summary.csv", index=False)
print("ODI match summary saved.")
