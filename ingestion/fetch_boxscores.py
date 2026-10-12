import json
import time
from pathlib import Path
import requests
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SEASON = 20232024  # change this and rerun for the other seasons

games = pd.read_csv(ROOT / "data" / "processed" / "games.csv")
ids = games.loc[games["season"] == SEASON, "game_id"].tolist()
print(len(ids), "games in season", SEASON)

out = ROOT / "data" / "raw" / "boxscores"
out.mkdir(parents=True, exist_ok=True)

downloaded = 0
failed = 0
for i, game_id in enumerate(ids, 1):
    path = out / f"{game_id}.json"
    if path.exists():
        continue
    url = f"https://api-web.nhle.com/v1/gamecenter/{game_id}/boxscore"
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        path.write_text(json.dumps(r.json()))
        downloaded += 1
    except requests.RequestException as e:
        failed += 1
        print(f"Failed {game_id}: {e}")
    time.sleep(0.5)
    if i % 100 == 0:
        print(f"{i}/{len(ids)} checked, {downloaded} downloaded, {failed} failed")

saved = sum(1 for g in ids if (out / f"{g}.json").exists())
print(f"Done. {saved}/{len(ids)} boxscores saved for season {SEASON}.")