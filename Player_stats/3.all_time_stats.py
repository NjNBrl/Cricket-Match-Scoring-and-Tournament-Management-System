import json
import os

TOURNAMENT_FILE = "Player_stats/tournament_stats.json"
ALL_TIME_FILE = "Player_stats/all_time_stats.json"

# Load all-time stats
if os.path.exists(ALL_TIME_FILE):
    with open(ALL_TIME_FILE, "r") as f:
        all_time = json.load(f)
else:
    all_time = []

# Load tournament stats
with open(TOURNAMENT_FILE, "r") as f:
    tournament = json.load(f)

# Convert to dictionary
players = {}

for p in all_time:
    key = (p["team_name"], p["player_name"])
    players[key] = p

# Add tournament totals
for p in tournament:

    key = (p["team_name"], p["player_name"])

    if key not in players:
        players[key] = p.copy()

    else:
        players[key]["matches"] += p["matches"]

        players[key]["runs"] += p["runs"]
        players[key]["balls"] += p["balls"]
        players[key]["fours"] += p["fours"]
        players[key]["sixes"] += p["sixes"]
        players[key]["strike_rate"] = players[key]["runs"]/players[key]["balls"]
        players[key]["average"] = players[key]["runs"]/players[key]["matches"]
        players[key]["wickets_taken"] += p["wickets_taken"]
        players[key]["balls_bowled"] += p["balls_bowled"]
        players[key]["runs_given"] += p["runs_given"]

        players[key]["highest_score"] = max(
            players[key]["highest_score"],
            p["highest_score"]
        )

# Save
with open(ALL_TIME_FILE, "w") as f:
    json.dump(list(players.values()), f, indent=4)