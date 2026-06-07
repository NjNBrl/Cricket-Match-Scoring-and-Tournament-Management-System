import json

with open("Player_stats/tournament_stats.json", "w") as f:
    json.dump([], f, indent=4)