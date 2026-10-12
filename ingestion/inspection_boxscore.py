import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "data" / "raw" / "boxscores" / "2023020031.json"
data = json.loads(path.read_text())

home = data["playerByGameStats"]["homeTeam"]
print("Home groups:", list(home.keys()))

for group in home:
    players = home[group]
    print(f"\n{group}: {len(players)} players")
    print("First record:", json.dumps(players[0], indent=2))

print("\ngameOutcome:", data["gameOutcome"])
