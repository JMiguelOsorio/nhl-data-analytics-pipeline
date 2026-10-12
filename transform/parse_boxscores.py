
import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
raw = ROOT / "data" / "raw" / "boxscores"
out = ROOT / "data" / "processed"
out.mkdir(parents=True, exist_ok=True)

SKATER_FIELDS = {
    "goals": "goals", "assists": "assists", "points": "points",
    "plusMinus": "plus_minus", "pim": "pim", "hits": "hits",
    "powerPlayGoals": "pp_goals", "sog": "shots", "blockedShots": "blocked_shots",
    "giveaways": "giveaways", "takeaways": "takeaways", "shifts": "shifts",
    "faceoffWinningPctg": "faceoff_pct",
}
GOALIE_FIELDS = {
    "shotsAgainst": "shots_against", "saves": "saves", "goalsAgainst": "goals_against",
    "savePctg": "save_pct", "powerPlayGoalsAgainst": "pp_goals_against",
    "starter": "starter", "decision": "decision", "pim": "pim",
}

def toi_to_minutes(toi):
    if not toi or ":" not in toi:
        return None
    minutes, seconds = toi.split(":")
    return int(minutes) + int(seconds) / 60

skaters, goalies, outcomes = [], [], []

for path in sorted(raw.glob("*.json")):
    d = json.loads(path.read_text())
    game_id = d["id"]
    outcomes.append({
        "game_id": game_id,
        "last_period_type": d.get("gameOutcome", {}).get("lastPeriodType"),
    })
    for side in ("homeTeam", "awayTeam"):
        team = d[side]["abbrev"]
        stats = d.get("playerByGameStats", {}).get(side, {})
        base = {"game_id": game_id, "team": team, "is_home": side == "homeTeam"}
        for group in ("forwards", "defense"):
            for p in stats.get(group, []):
                row = {**base, "player_id": p["playerId"],
                       "player_name": p["name"]["default"], "position": p.get("position")}
                for src, dst in SKATER_FIELDS.items():
                    row[dst] = p.get(src)
                row["toi_minutes"] = toi_to_minutes(p.get("toi"))
                skaters.append(row)
        for p in stats.get("goalies", []):
            row = {**base, "player_id": p["playerId"], "player_name": p["name"]["default"]}
            for src, dst in GOALIE_FIELDS.items():
                row[dst] = p.get(src)
            row["toi_minutes"] = toi_to_minutes(p.get("toi"))
            goalies.append(row)

tables = {
    "skater_game_stats": pd.DataFrame(skaters),
    "goalie_game_stats": pd.DataFrame(goalies),
    "game_outcomes": pd.DataFrame(outcomes),
}
for name, df in tables.items():
    df.to_csv(out / f"{name}.csv", index=False)
    print(f"{name}: {len(df)} rows, {df.shape[1]} columns")

print(tables["game_outcomes"]["last_period_type"].value_counts())

