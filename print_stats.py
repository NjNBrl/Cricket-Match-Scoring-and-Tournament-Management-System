import json
from PIL import Image, ImageDraw, ImageFont

# ---------- INPUT ----------
json_file = "Player_stats/tournament_stats.json"
stat_key = input(
    "Enter stat (runs, strike_rate, average, fours, sixes, wickets_taken, runs_given): "
).strip()

# ---------- LOAD DATA ----------
with open(json_file, "r") as f:
    players = json.load(f)

# ---------- VALIDATION ----------
valid_keys = [
    "runs",
    "strike_rate",
    "average",
    "fours",
    "sixes",
    "wickets_taken",
    "runs_given"
]

if stat_key not in valid_keys:
    print("Invalid stat.")
    exit()

# ---------- SORT ----------
if stat_key == "runs_given":
    ranked = sorted(players, key=lambda x: x[stat_key])  # lower better
else:
    ranked = sorted(players, key=lambda x: x[stat_key], reverse=True)

# ---------- IMAGE SETTINGS ----------
WIDTH = 1000
ROW_HEIGHT = 60
HEADER_HEIGHT = 80
HEIGHT = HEADER_HEIGHT + len(ranked) * ROW_HEIGHT + 40

img = Image.new("RGB", (WIDTH, HEIGHT), (25, 25, 25))
draw = ImageDraw.Draw(img)

# ---------- FONT ----------
try:
    title_font = ImageFont.truetype("arial.ttf", 40)
    header_font = ImageFont.truetype("arial.ttf", 28)
    row_font = ImageFont.truetype("arial.ttf", 24)
except:
    title_font = ImageFont.load_default()
    header_font = ImageFont.load_default()
    row_font = ImageFont.load_default()

# ---------- TITLE ----------
title = f"{stat_key.upper()} LEADERBOARD"
draw.text((20, 15), title, fill="gold", font=title_font)

# ---------- HEADERS ----------
y = HEADER_HEIGHT

draw.rectangle([0, y, WIDTH, y + 40], fill=(45, 45, 45))

draw.text((30, y + 5), "Rank", fill="white", font=header_font)
draw.text((130, y + 5), "Player", fill="white", font=header_font)
draw.text((450, y + 5), "Team", fill="white", font=header_font)
draw.text((700, y + 5), stat_key.upper(), fill="white", font=header_font)

# ---------- ROWS ----------
y += 50

for rank, player in enumerate(ranked, start=1):

    if rank == 1:
        bg = (60, 50, 0)
    elif rank == 2:
        bg = (50, 50, 50)
    elif rank == 3:
        bg = (70, 40, 20)
    else:
        bg = (35, 35, 35)

    draw.rectangle(
        [10, y, WIDTH - 10, y + ROW_HEIGHT - 5],
        fill=bg
    )

    draw.text((40, y + 15), str(rank), fill="white", font=row_font)
    draw.text((130, y + 15), player["player_name"], fill="white", font=row_font)
    draw.text((450, y + 15), player["team_name"], fill="white", font=row_font)
    draw.text((720, y + 15), str(player[stat_key]), fill="gold", font=row_font)

    y += ROW_HEIGHT

# ---------- SAVE ----------
output_file = f"{stat_key}_leaderboard.png"
img.save(output_file)

print(f"Saved: {output_file}")