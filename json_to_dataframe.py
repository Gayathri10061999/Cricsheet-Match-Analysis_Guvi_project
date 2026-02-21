import json
import pandas as pd
import os

DATA_DIR = "C:/Users/gayat/AppData/Local/Programs/Python/Python313/t20s_json"

matches = []
deliveries = []

for file in os.listdir(DATA_DIR):
    if file.endswith(".json"):
        with open(os.path.join(DATA_DIR, file), "r") as f:
            data = json.load(f)

        match_id = file.replace(".json", "")
        info = data["info"]

        matches.append({
            "match_id": match_id,
            "date": info["dates"][0],
            "venue": info.get("venue"),
            "team1": info["teams"][0],
            "team2": info["teams"][1],
            "winner": info.get("outcome", {}).get("winner"),
            "match_type": info["match_type"]
        })

        for inning in data["innings"]:
            batting_team = inning["team"]

            for over in inning["overs"]:
                for ball in over["deliveries"]:
                    deliveries.append({
                        "match_id": match_id,
                        "batting_team": batting_team,
                        "batter": ball["batter"],
                        "bowler": ball["bowler"],
                        "runs": ball["runs"]["batter"],
                        "extras": ball["runs"]["extras"]
                    })

matches_df = pd.DataFrame(matches)
deliveries_df = pd.DataFrame(deliveries)
matches_df.to_csv("C:/Users/gayat/AppData/Local/Programs/Python/Python313/processed_matches.csv", index=False)
deliveries_df.to_csv("C:/Users/gayat/AppData/Local/Programs/Python/Python313/processed_deliveries.csv", index=False)

print("Data transformation completed.")

print(matches_df.head())
print(deliveries_df.head())
