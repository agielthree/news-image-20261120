#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news poster (1024x1024, deterministic).

Run: python3 draw_poster.py  -> writes entry.png next to this script.
The PNG is fully deterministic: fixed palette, fixed fonts, fixed layout,
no timestamps embedded by Pillow, so repeated runs are byte-identical.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (18, 38, 63)
GOLD = (212, 175, 55)
PAPER = (245, 241, 232)
CARD = (255, 255, 255)
INK = (24, 30, 38)
GREY = (110, 116, 124)
WHITE = (255, 255, 255)

STORIES = [
    ("1", "LAW  ·  THE HAGUE", (31, 93, 140),
     "ICJ finds Myanmar guilty of genocide against Rohingya",
     "The court rules 9-6 that Myanmar committed genocide "
     "against the Rohingya, a first for any state at the ICJ.",
     "Source: CNN"),
    ("2", "WEATHER  ·  INDIA", (27, 110, 90),
     "Cyclone Akvan slams India's east coast",
     "Cyclone Akvan makes landfall near Gopalpur, Odisha, "
     "with 90\u2013110 km/h winds; over 300,000 people are evacuated.",
     "Source: IANS"),
    ("3", "EUROPE  ·  KYIV", (146, 46, 46),
     "Russian strike damages EU embassies in Kyiv",
     "Projectiles damage the Austrian and Dutch embassies in "
     "Kyiv; the EU and European states summon Russia's envoys.",
     "Source: Reuters"),
    ("4", "DIPLOMACY  ·  SHENZHEN", (31, 93, 140),
     "Trump, Xi and Putin hold first three-way summit",
     "The three leaders meet in Shenzhen and issue a joint "
     "peace declaration; Putin rules out a ceasefire with Ukraine.",
     "Source: The Times"),
    ("5", "HORN OF AFRICA  ·  MOGADISHU", (146, 46, 46),
     "Somalia expels UAE ambassador in 72 hours",
     "Somalia orders the UAE ambassador out in 72 hours "
     "and recalls its own envoy over violations of its sovereignty.",
     "Source: Reuters"),
    ("6", "EUROPE  ·  UKRAINE", (27, 110, 90),
     "European leaders ready to talk with Russia",
     "European leaders say they are ready to negotiate with "
     "Russia to bring the war in Ukraine to an end.",
     "Source: BBC"),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- header band ----
    d.rectangle([0, 0, W, 172], fill=NAVY)
    d.rectangle([0, 172, W, 178], fill=GOLD)
    d.text((36, 26), "THE WORLD IN ONE DAY", font=font(FONT_BOLD, 58), fill=WHITE)
    d.text((36, 96), "Friday, 20 November 2026",
           font=font(FONT_BOLD, 34), fill=GOLD)
    d.text((36, 140), "Six stories that defined the day",
           font=font(FONT_REG, 22), fill=(200, 210, 222))

    # ---- story grid: 2 cols x 3 rows ----
    margin, gap = 28, 18
    top, bottom = 196, 962
    cw = (W - 2 * margin - gap) // 2
    ch = (bottom - top - 2 * gap) // 3
    for i, (num, kicker, accent, headline, body, source) in enumerate(STORIES):
        x = margin + (i % 2) * (cw + gap)
        y = top + (i // 2) * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=14, fill=CARD,
                            outline=(214, 210, 198), width=1)
        d.rectangle([x, y + 14, x + 8, y + ch - 14], fill=accent)
        # number badge
        d.ellipse([x + 24, y + 20, x + 64, y + 60], fill=accent)
        d.text((x + 44, y + 39), num, font=font(FONT_BOLD, 24),
               fill=WHITE, anchor="mm")
        d.text((x + 78, y + 38), kicker, font=font(FONT_BOLD, 17),
               fill=accent, anchor="lm")
        # headline, up to 2 lines
        hl = wrap(d, headline, font(FONT_BOLD, 25), cw - 48)
        hy = y + 74
        for line in hl[:2]:
            d.text((x + 24, hy), line, font=font(FONT_BOLD, 25), fill=INK)
            hy += 31
        # body, up to 3 lines
        bl = wrap(d, body, font(FONT_REG, 19), cw - 48)
        by = hy + 6
        for line in bl[:3]:
            d.text((x + 24, by), line, font=font(FONT_REG, 19), fill=(58, 64, 74))
            by += 25
        d.text((x + 24, y + ch - 30), source, font=font(FONT_REG, 15), fill=GREY)

    # ---- footer ----
    d.text((W // 2, 986),
           "Sources: CNN  ·  Reuters  ·  The Times  ·  IANS  ·  BBC  —  Events of 20 November 2026, as reported that day",
           font=font(FONT_REG, 16), fill=GREY, anchor="mm")

    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
