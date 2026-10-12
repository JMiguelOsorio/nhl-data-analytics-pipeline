import json
from pathlib import Path
import requests
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

games = pd.read_csv(ROOT / "data" / "processed" / "games.csv")
game_id = int(games["game_id"].iloc[0])
print("Game:", game_id)

url = f"https://api-web.nhle.com/v1/gamecenter/{game_id}/boxscore"
r = requests.get(url, timeout=30)
print("Status:", r.status_code)

data = r.json()
print("Top-level keys:", list(data.keys()))
print("homeTeam keys:", list(data["homeTeam"].keys()))
print("playerByGameStats keys:", list(data.get("playerByGameStats", {}).keys()))

out = ROOT / "data" / "raw" / "boxscores"
out.mkdir(parents=True, exist_ok=True)
(out / f"{game_id}.json").write_text(json.dumps(data, indent=2))
print("Saved to", out / f"{game_id}.json")