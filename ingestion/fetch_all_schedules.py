import json
import time
from pathlib import Path
import requests
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SEASONS = ["20232024", "20242025", "20252026"]

raw_dir = ROOT / "data" / "raw" / "schedules"
raw_dir.mkdir(parents=True, exist_ok=True)

standings = json.loads((ROOT / "data" / "raw" / "standings_now.json").read_text())
teams = sorted({t["teamAbbrev"]["default"] for t in standings["standings"]} | {"ARI"})
print(len(teams), "teams to try:", teams)

rows = []
for season in SEASONS:
    for abbr in teams:
        url = f"https://api-web.nhle.com/v1/club-schedule-season/{abbr}/{season}"
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"Skipping {abbr} {season} (status {r.status_code})")
            continue
        data = r.json()
        if not data.get("games"):
            print(f"Skipping {abbr} {season} (no games)")
            continue
        (raw_dir / f"{abbr}_{season}.json").write_text(json.dumps(data))
        for g in data["games"]:
            rows.append({
                "game_id": g["id"],
                "season": g["season"],
                "game_type": g["gameType"],
                "game_date": g["gameDate"],
                "game_state": g["gameState"],
                "home_team": g["homeTeam"]["abbrev"],
                "home_score": g["homeTeam"].get("score"),
                "away_team": g["awayTeam"]["abbrev"],
                "away_score": g["awayTeam"].get("score"),
            })
        time.sleep(0.5)

df = pd.DataFrame(rows)
print("Raw rows:", len(df))

df = df.drop_duplicates(subset="game_id")
print("After removing duplicates:", len(df))

df = df[(df["game_type"] == 2) & (df["game_state"].isin(["FINAL", "OFF"]))]
print("Regular season, finished games:", len(df))
print(df.groupby("season").size())

out = ROOT / "data" / "processed"
out.mkdir(parents=True, exist_ok=True)
df.to_csv(out / "games.csv", index=False)
print("Saved to", out / "games.csv")