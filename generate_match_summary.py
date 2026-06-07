import json
import glob
from PIL import Image, ImageDraw, ImageFont

# ---------- INPUT ----------
tournament_name = input("Enter tournament name: ")

innings_1_batting_file = glob.glob(f"{tournament_name}/1.*_batting.json")[0]
innings_1_bowling_file = glob.glob(f"{tournament_name}/1.*_bowling.json")[0]

innings_2_batting_file = glob.glob(f"{tournament_name}/2.*_batting.json")[0]
innings_2_bowling_file = glob.glob(f"{tournament_name}/2.*_bowling.json")[0]


# ---------- LOAD ----------
def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


# ---------- SORT HELPERS ----------
def get_top_batters(data, n=3):
    return sorted(data, key=lambda x: (x["runs"], x["strike_rate"]), reverse=True)[:n]


def get_top_bowlers(data, n=3):
    return sorted(data, key=lambda x: (x["wickets_taken"], -x["runs_given"]), reverse=True)[:n]


# ---------- DRAW CARD ----------
def draw_section(draw, x, y, w, h, bg_color, title, text_lines, font_title, font_text):
    # background box
    draw.rectangle([x, y, x + w, y + h], fill=bg_color)

    padding = 20
    text_x = x + padding
    text_y = y + padding

    # title
    draw.text((text_x, text_y), title, fill="white", font=font_title)
    text_y += 50

    # body
    for line in text_lines:
        draw.text((text_x, text_y), line, fill="white", font=font_text)
        text_y += 28


# ---------- BUILD TEXT BLOCK ----------
def build_block(batting_data, bowling_data):
    batting_team = batting_data[0]["team_name"]
    bowling_team = bowling_data[0]["team_name"]

    lines = []

    lines.append(f"Top Batters ({batting_team})")
    for i, b in enumerate(get_top_batters(batting_data), 1):
        lines.append(f"{b['name']}  -  {b['runs']}({b['balls']})")

    lines.append("")
    lines.append(f"Top Bowlers ({bowling_team})")
    for i, b in enumerate(get_top_bowlers(bowling_data), 1):
        lines.append(f"{b['name']}  -  {b['wickets_taken']}/{b['runs_given']}")

    return lines


# ---------- LOAD DATA ----------
innings_1_batting = load_json(innings_1_batting_file)
innings_1_bowling = load_json(innings_1_bowling_file)

innings_2_batting = load_json(innings_2_batting_file)
innings_2_bowling = load_json(innings_2_bowling_file)


team1 = innings_1_batting[0]["team_name"]
team2 = innings_2_batting[0]["team_name"]

score1 = f"{team1} {innings_1_batting[0]['team_total']}/{innings_1_batting[0]['wickets']} ({innings_1_batting[0]['overs']})"
score2 = f"{team2} {innings_2_batting[0]['team_total']}/{innings_2_batting[0]['wickets']} ({innings_2_batting[0]['overs']})"


# ---------- IMAGE ----------
W, H = 1100, 1400
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# fonts
try:
    title_font = ImageFont.truetype("arial.ttf", 40)
    section_font = ImageFont.truetype("arial.ttf", 26)
    text_font = ImageFont.truetype("arial.ttf", 22)
except:
    title_font = ImageFont.load_default()
    section_font = ImageFont.load_default()
    text_font = ImageFont.load_default()


# ---------- HEADER ----------
draw.rectangle([0, 0, W, 120], fill="black")
draw.text((30, 35), f"MATCH SUMMARY: {team1} vs {team2}", fill="white", font=title_font)


# ---------- SECTION 1 (RED) ----------
block1 = build_block(innings_1_batting, innings_1_bowling)
draw_section(
    draw,
    x=40,
    y=160,
    w=W - 80,
    h=520,
    bg_color="#C0392B",  # deep red
    title=f"1st Innings - {score1}",
    text_lines=block1,
    font_title=section_font,
    font_text=text_font
)


# ---------- SECTION 2 (BLUE) ----------
block2 = build_block(innings_2_batting, innings_2_bowling)
draw_section(
    draw,
    x=40,
    y=720,
    w=W - 80,
    h=520,
    bg_color="#1F4E79",  # deep blue
    title=f"2nd Innings - {score2}",
    text_lines=block2,
    font_title=section_font,
    font_text=text_font
)


# ---------- SAVE ----------
filename = f"{team1} vs {team2} match_summary.png"
img.save(filename)

print(f"Saved: {filename}")