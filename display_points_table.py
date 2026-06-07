import json
from PIL import Image, ImageDraw, ImageFont

# ---------- INPUT ----------
tournament_name = input("Enter tournament name: ")

with open(f"{tournament_name}/points_table.json", "r") as file:
    points_table = json.load(file)

# ---------- PROCESS ----------
teams = []
for team in points_table:
    if not team["team_name"].strip():
        continue

    team["points"] = team["wins"] * 2
    teams.append(team)

teams.sort(key=lambda x: (x["points"], x["run_rate"]), reverse=True)


# ---------- IMAGE SETUP ----------
W, H = 1200, 800 + len(teams) * 60
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

try:
    title_font = ImageFont.truetype("arial.ttf", 40)
    header_font = ImageFont.truetype("arial.ttf", 22)
    text_font = ImageFont.truetype("arial.ttf", 20)
except:
    title_font = ImageFont.load_default()
    header_font = ImageFont.load_default()
    text_font = ImageFont.load_default()


# ---------- TITLE ----------
draw.rectangle([0, 0, W, 90], fill="black")
draw.text((30, 25), f"{tournament_name.upper()} - POINTS TABLE", fill="white", font=title_font)


# ---------- COLUMN HEADERS ----------
start_y = 120
draw.rectangle([20, start_y, W - 20, start_y + 50], fill="#2C3E50")

headers = ["Pos", "Team", "Mat", "Won", "Lost", "Pts", "RF", "OF", "RA", "OC", "NRR"]

x_positions = [30, 90, 300, 360, 420, 500, 580, 660, 740, 820, 920]

for i, h in enumerate(headers):
    draw.text((x_positions[i], start_y + 15), h, fill="white", font=header_font)


# ---------- ROWS ----------
y = start_y + 60

for pos, team in enumerate(teams, start=1):
    matches = team["wins"] + team["loss"]

    # highlight top 3
    if pos == 1:
        bg = "#27AE60"   # green (leader)
    elif pos == 2:
        bg = "#2980B9"   # blue
    elif pos == 3:
        bg = "#8E44AD"   # purple
    else:
        bg = "#ECF0F1" if pos % 2 == 0 else "#D5DBDB"

    draw.rectangle([20, y, W - 20, y + 50], fill=bg)

    color = "white" if pos <= 3 else "black"

    row = [
        str(pos),
        team["team_name"],
        str(matches),
        str(team["wins"]),
        str(team["loss"]),
        str(team["points"]),
        str(team["runs_for"]),
        str(team["overs_played"]),
        str(team["runs_against"]),
        str(team["overs_conceded"]),
        f"{team['run_rate']:.2f}"
    ]

    for i, val in enumerate(row):
        draw.text((x_positions[i], y + 15), val, fill=color, font=text_font)

    y += 60


# ---------- SAVE ----------
filename = f"{tournament_name}_points_table.png"
img.save(filename)

print(f"Saved: {filename}")