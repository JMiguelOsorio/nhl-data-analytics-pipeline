# import json
# import requests
# from pathlib import Path

# url = "https://statsapi.mlb.com/api/v1/standings?leagueId=103,104&season=2025"
# r = requests.get(url, timeout=30)
# print("status: ", r.status_code)

# data = r.json()
# print("level keys:", list(data.keys()))




import json
from pathlib import Path
import requests

url = "https://api-web.nhle.com/v1/club-schedule-season/TOR/20242025"
r = requests.get(url, timeout=30)
print("Status:", r.status_code)

data = r.json()
print("Top-level keys:", list(data.keys()))
print("Games returned:", len(data["games"]))
print("First game:", json.dumps(data["games"][0], indent=2)[:1500])

out = Path("data/raw")
out.mkdir(parents=True, exist_ok=True)
(out / "schedule_TOR_20242025.json").write_text(json.dumps(data, indent=2))