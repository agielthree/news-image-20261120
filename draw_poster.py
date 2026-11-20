#!/usr/bin/env python3
"""Render the 20 November 2026 world-news poster as a 1024x1024 PNG.

The script is deterministic by construction: a fixed palette, fixed
DejaVu fonts, fixed geometry and no timestamps anywhere, so running it
twice yields byte-identical output.

Usage: python3 draw_poster.py   (writes entry.png beside the script)
"""

from dataclasses import dataclass
from os.path import getsize

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
DEJAVU_DIR = "/usr/share/fonts/truetype/dejavu/"

PALETTE = {
    "navy": (18, 38, 63),
    "gold": (212, 175, 55),
    "paper": (245, 241, 232),
    "card": (255, 255, 255),
    "ink": (24, 30, 38),
    "body": (58, 64, 74),
    "grey": (110, 116, 124),
    "white": (255, 255, 255),
    "line": (214, 210, 198),
    "subhead": (200, 210, 222),
}


@dataclass
class Story:
    tag: str
    tint: tuple
    title: str
    text: str
    credit: str


STORIES = [
    Story(
        tag="LAW  ·  THE HAGUE",
        tint=(31, 93, 140),
        title="ICJ finds Myanmar guilty of genocide against Rohingya",
        text="The court rules 9-6 that Myanmar committed genocide "
        "against the Rohingya, a first for any state at the ICJ.",
        credit="Source: CNN",
    ),
    Story(
        tag="WEATHER  ·  INDIA",
        tint=(27, 110, 90),
        title="Cyclone Akvan slams India's east coast",
        text="Cyclone Akvan makes landfall near Gopalpur, Odisha, "
        "with 90–110 km/h winds; over 300,000 people are evacuated.",
        credit="Source: IANS",
    ),
    Story(
        tag="EUROPE  ·  KYIV",
        tint=(146, 46, 46),
        title="Russian strike damages EU embassies in Kyiv",
        text="Projectiles damage the Austrian and Dutch embassies in "
        "Kyiv; the EU and European states summon Russia's envoys.",
        credit="Source: Reuters",
    ),
    Story(
        tag="DIPLOMACY  ·  SHENZHEN",
        tint=(31, 93, 140),
        title="Trump, Xi and Putin hold first three-way summit",
        text="The three leaders meet in Shenzhen and issue a joint "
        "peace declaration; Putin rules out a ceasefire with Ukraine.",
        credit="Source: The Times",
    ),
    Story(
        tag="HORN OF AFRICA  ·  MOGADISHU",
        tint=(146, 46, 46),
        title="Somalia expels UAE ambassador in 72 hours",
        text="Somalia orders the UAE ambassador out in 72 hours "
        "and recalls its own envoy over violations of its sovereignty.",
        credit="Source: Reuters",
    ),
    Story(
        tag="EUROPE  ·  UKRAINE",
        tint=(27, 110, 90),
        title="European leaders ready to talk with Russia",
        text="European leaders say they are ready to negotiate with "
        "Russia to bring the war in Ukraine to an end.",
        credit="Source: BBC",
    ),
]


def load(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(DEJAVU_DIR + name, size)


def fit_lines(draw, text, font, width):
    """Greedy word wrap measured in pixels; returns a list of lines."""
    out = []
    line = ""
    for word in text.split():
        joined = (line + " " + word).strip()
        if draw.textlength(joined, font=font) <= width:
            line = joined
            continue
        if line:
            out.append(line)
        line = word
    if line:
        out.append(line)
    return out


def paint_header(draw):
    draw.rectangle((0, 0, W, 172), fill=PALETTE["navy"])
    draw.rectangle((0, 172, W, 178), fill=PALETTE["gold"])
    draw.text((36, 26), "THE WORLD IN ONE DAY",
              font=load(58, bold=True), fill=PALETTE["white"])
    draw.text((36, 96), "Friday, 20 November 2026",
              font=load(34, bold=True), fill=PALETTE["gold"])
    draw.text((36, 140), "Six stories that defined the day",
              font=load(22), fill=PALETTE["subhead"])


def paint_story(draw, story, index, card_w, card_h):
    margin, gutter, top = 28, 18, 196
    x = margin + (index % 2) * (card_w + gutter)
    y = top + (index // 2) * (card_h + gutter)
    draw.rounded_rectangle((x, y, x + card_w, y + card_h), radius=14,
                           fill=PALETTE["card"], outline=PALETTE["line"],
                           width=1)
    draw.rectangle((x, y + 14, x + 8, y + card_h - 14), fill=story.tint)
    # Numbered badge and section tag.
    draw.ellipse((x + 24, y + 20, x + 64, y + 60), fill=story.tint)
    draw.text((x + 44, y + 39), str(index + 1), font=load(24, bold=True),
              fill=PALETTE["white"], anchor="mm")
    draw.text((x + 78, y + 38), story.tag, font=load(17, bold=True),
              fill=story.tint, anchor="lm")
    # Headline, at most two lines; body, at most three.
    head = fit_lines(draw, story.title, load(25, bold=True), card_w - 48)
    hy = y + 74
    for line in head[:2]:
        draw.text((x + 24, hy), line, font=load(25, bold=True),
                  fill=PALETTE["ink"])
        hy += 31
    body = fit_lines(draw, story.text, load(19), card_w - 48)
    by = hy + 6
    for line in body[:3]:
        draw.text((x + 24, by), line, font=load(19),
                  fill=PALETTE["body"])
        by += 25
    draw.text((x + 24, y + card_h - 30), story.credit, font=load(15),
              fill=PALETTE["grey"])


def paint_footer(draw):
    note = ("Sources: CNN  ·  Reuters  ·  The Times  ·  IANS  ·  BBC  —  "
            "Events of 20 November 2026, as reported that day")
    draw.text((W // 2, 986), note, font=load(16),
              fill=PALETTE["grey"], anchor="mm")


def build():
    img = Image.new("RGB", (W, H), PALETTE["paper"])
    draw = ImageDraw.Draw(img)
    paint_header(draw)
    card_w = (W - 2 * 28 - 18) // 2
    card_h = (962 - 196 - 2 * 18) // 3
    for i, story in enumerate(STORIES):
        paint_story(draw, story, i, card_w, card_h)
    paint_footer(draw)
    img.save("entry.png", format="PNG", optimize=True)
    # The gate caps the entry at 1 MiB and 1024x1024: fail loudly here
    # rather than shipping an entry the gate would reject.
    assert img.size == (W, H)
    assert getsize("entry.png") <= 1048576


if __name__ == "__main__":
    build()
