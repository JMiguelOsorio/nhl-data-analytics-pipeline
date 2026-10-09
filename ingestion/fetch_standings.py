import json
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]

url = "https://api-web.nhle.com/v1/standings/now"
r = requests.get(url, timeout=30)
print("Status:", r.status_code)

data = r.json()
print("Teams returned:", len(data["standings"]))

out = ROOT / "data" / "raw"
out.mkdir(parents=True, exist_ok=True)
(out / "standings_now.json").write_text(json.dumps(data, indent=2))
print("Saved to", out / "standings_now.json")