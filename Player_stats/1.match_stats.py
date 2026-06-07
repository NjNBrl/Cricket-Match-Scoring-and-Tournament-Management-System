import json
import os
import glob

tournament_name = input("Enter tournament name: ")

# Load files
innings1_batting = json.load(open(glob.glob(f"{tournament_name}/1.*_batting.json")[0]))
innings1_bowling = json.load(open(glob.glob(f"{tournament_name}/1.*_bowling.json")[0]))

innings2_batting = json.load(open(glob.glob(f"{tournament_name}/2.*_batting.json")[0]))
innings2_bowling = json.load(open(glob.glob(f"{tournament_name}/2.*_bowling.json")[0]))

combined = []

# Team batting first
bowling_lookup = {
    p["name"]: p
    for p in innings2_bowling
}

for batter in innings1_batting:
    bowler = bowling_lookup.get(batter["name"], {})

    combined.append({
        "team_name": batter["team_name"],
        "player_name": batter["name"],
        "runs": batter["runs"],
        "balls": batter["balls"],
        "fours": batter["fours"],
        "sixes": batter["sixes"],
        "strike_rate": round(batter["runs"] / batter["balls"] * 100, 2)
                        if batter["balls"] else 0,
        "wickets_taken": bowler.get("wickets_taken", 0),
        "overs": bowler.get("overs", 0),
        "runs_given": bowler.get("runs_given", 0)
    })

# Team batting second
bowling_lookup = {
    p["name"]: p
    for p in innings1_bowling
}

for batter in innings2_batting:
    bowler = bowling_lookup.get(batter["name"], {})

    combined.append({
        "team_name": batter["team_name"],
        "player_name": batter["name"],
        "runs": batter["runs"],
        "balls": batter["balls"],
        "fours": batter["fours"],
        "sixes": batter["sixes"],
        "strike_rate": round(batter["runs"] / batter["balls"] * 100, 2)
                        if batter["balls"] else 0,
        "wickets_taken": bowler.get("wickets_taken", 0),
        "overs": bowler.get("overs", 0),
        "runs_given": bowler.get("runs_given", 0)
    })

with open("Player_stats/match_stats.json", "w") as f:
    json.dump(combined, f, indent=4)

print(f"Combined {len(combined)} player records")
files_to_delete = [
    glob.glob(f"{tournament_name}/1.*_batting.json")[0],
    glob.glob(f"{tournament_name}/1.*_bowling.json")[0],
    glob.glob(f"{tournament_name}/2.*_batting.json")[0],
    glob.glob(f"{tournament_name}/2.*_bowling.json")[0],
]

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"Deleted: {file}")