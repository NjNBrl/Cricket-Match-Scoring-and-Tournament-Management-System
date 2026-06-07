import json
import os

MATCH_FILE = "Player_stats/match_stats.json"
TOURNAMENT_FILE = "Player_stats/tournament_stats.json"

# Load tournament stats if exists
if os.path.exists(TOURNAMENT_FILE):
    with open(TOURNAMENT_FILE, "r") as f:
        tournament_stats = json.load(f)
else:
    tournament_stats = []

# Convert tournament stats to dictionary
players = {}

for p in tournament_stats:
    key = (p["team_name"], p["player_name"])
    players[key] = p

# Load current match stats
with open(MATCH_FILE, "r") as f:
    match_stats = json.load(f)

# Update tournament stats
for p in match_stats:

    key = (p["team_name"], p["player_name"])

    if key not in players:
        players[key] = {
            "team_name": p["team_name"],
            "player_name": p["player_name"],
            "matches": 0,

            "runs": 0,
            "balls": 0,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 0.0,
            "wickets_taken": 0,
            "balls_bowled": 0,
            "runs_given": 0,
            "average" : 0,
            "highest_score": 0,
            "best_bowling_wickets": 0,
            "best_bowling_runs": 999
        }

    player = players[key]

    player["matches"] += 1
    player["runs"] += p["runs"]
    player["balls"] += p["balls"]
    player["fours"] += p["fours"]
    player["sixes"] += p["sixes"]
    player["strike_rate"] = player["runs"]/player["balls"]
    player["average"] = player["runs"]/player["matches"]
    player["wickets_taken"] += p["wickets_taken"]
    player["runs_given"] += p["runs_given"]

    # Convert overs to balls
    overs = int(p["overs"])
    balls = round((p["overs"] - overs) * 10)

    balls_bowled = overs * 6 + balls

    player["balls_bowled"] += balls_bowled

    # Records
    player["highest_score"] = max(
        player["highest_score"],
        p["runs"]
    )

    if p["wickets_taken"] > player["best_bowling_wickets"]:
        player["best_bowling_wickets"] = p["wickets_taken"]
        player["best_bowling_runs"] = p["runs_given"]

    elif p["wickets_taken"] == player["best_bowling_wickets"]:
        player["best_bowling_runs"] = min(
            player["best_bowling_runs"],
            p["runs_given"]
        )

# Save back
with open(TOURNAMENT_FILE, "w") as f:
    json.dump(list(players.values()), f, indent=4)

print("Tournament stats updated.")