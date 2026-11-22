# news-image-20261122 -- Agent 2 (noble-robin-77), 3/3 entry: "TAGGED".
# Sunday 22 November 2026, 38 stories. Drawn from scratch with Pillow.
# Signature: every story carries a status tag -- ONGOING (red) / REPORTED
# (blue) / CLAIM (amber) -- explained in a legend under the masthead, and
# the ALSO list runs in two columns with a region tag on every line.
# Cream paper, red masthead, 3 dramatic heroes (COP31, Ukraine-148,
# Bahrain), 10 small panels, a real equirectangular world map with 13
# numbered pins on land, a region bar totalling exactly 38, and a red
# DATE CHECK box. No dark pages.
#
# Facts verified before this render (strategy 3/3, 22 Nov ~16:30 WIB):
# COP31 final text tabled early Sunday, approval session 06:00 GMT, no
# fossil-fuel mention, 35% clean power by 2035, $120bn goal dropped,
# quorum fear -- so panel 1 says "nears a deal" and DATE CHECK lists the
# final approval as not yet happened. Ukraine barrage tonight: 148
# drones, 2 killed / 60 hurt in Kryvyi Rih, 161 shot down. F1: Verstappen
# WON Las Vegas (not pole). Hong Kong turnout 89.81%.

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
CREAM = (247, 243, 232)
PAPER = (252, 249, 241)
PANEL_BG = (255, 253, 247)
INK = (28, 24, 20)
GREY = (110, 104, 92)
LINE = (190, 182, 166)
RED = (178, 34, 28)
BLUE = (46, 95, 138)
AMBER = (176, 118, 18)
GOLD = (192, 138, 26)
MAP_BG = (238, 234, 220)
LAND = (214, 205, 186)
LAND_LINE = (168, 158, 138)

SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"

TAG_COL = {"ONGOING": RED, "REPORTED": BLUE, "CLAIM": AMBER}

REG_COL = {
    "Europe": (46, 95, 138),
    "M. East": (179, 55, 47),
    "Asia": (192, 138, 26),
    "Americas": (62, 122, 78),
    "Africa": (122, 92, 158),
    "Oceania": (46, 122, 122),
    "Global": (110, 110, 110),
}

STATS = [
    ("148", "DRONES OVER UKRAINE"),
    ("16", "SPARTA II CREW SAVED"),
    ("2", "PATRIOT RADARS HIT"),
    ("1,661", "GAZA DEATH TOLL"),
    ("89.81%", "HONG KONG TURNOUT"),
    ("720/9", "INDIA DECLARE"),
]

# (num, kicker, title, body, region, tag, scene)
HEROES = [
    (1, "ANTALYA \u00b7 CLIMATE",
     "COP31 nears a deal as approval opens",
     "Final text tabled early Sunday; no fossil-fuel mention; 35% clean "
     "power by 2035; $120bn goal dropped.",
     "Europe", "ONGOING", "cop31"),
    (2, "KRYVYI RIH \u00b7 WAR",
     "148 drones hit Ukraine overnight",
     "2 killed, 60 hurt in Kryvyi Rih; 161 drones shot down; 3 missiles, "
     "12 glide bombs.",
     "Europe", "REPORTED", "ukraine"),
    (3, "BAHRAIN \u00b7 IRAN WAR",
     "Iran says it struck two US bases",
     "Tehran claims 2 Patriot radars hit; Bahrain: most intercepted; "
     "1 site burned, no deaths.",
     "M. East", "CLAIM", "bahrain"),
]

# (num, kicker, title, body, region, tag)
PANELS = [
    (4, "GULF OF FINLAND",
     "Russian ship still burning off Finland",
     "16 crew evacuated; fire still burns.",
     "Europe", "ONGOING"),
    (5, "HONG KONG",
     "856 candidates chase 723 seats",
     "Turnout 89.81% by 13:00.",
     "Asia", "REPORTED"),
    (6, "HORMUZ",
     "Two tankers hit leaving Hormuz",
     "Torkel still burning at anchor.",
     "M. East", "REPORTED"),
    (7, "WELLINGTON",
     "Pant 128, Rahul 136; India declare 720/9",
     "Lead 352; NZ 105/2 at stumps.",
     "Oceania", "REPORTED"),
    (8, "LAS VEGAS",
     "Verstappen wins the Las Vegas GP",
     "Third win in four years; Norris 2nd, Piastri 3rd.",
     "Americas", "REPORTED"),
    (9, "TEHRAN",
     "Iran starts rationing power, 2 hours a day",
     "Gas output lags; blackouts from Sunday.",
     "M. East", "ONGOING"),
    (10, "GAZA",
     "Four killed as Gaza ceasefire frays",
     "Aid van hit; Hamas seeks emergency talks.",
     "M. East", "ONGOING"),
    (11, "SINALOA",
     "Mexico captures \u2018El Chapo Isidro\u2019",
     "Top-10 FBI fugitive held; 11 killed.",
     "Americas", "REPORTED"),
    (12, "BAYELSA",
     "Mourners\u2019 boat capsizes, 24 dead",
     "Boat carrying funeral-goers overturns.",
     "Africa", "REPORTED"),
    (13, "DARMSTADT",
     "BepiColombo enters orbit around Mercury",
     "ESA craft sends its first photos.",
     "Europe", "REPORTED"),
]

# ALSO list: the 25 pool stories that are not panels, by pool number,
# two columns, each line carrying its region tag.
# (pool num, title, region)
ALSO = [
    (11, "Power-plant fire kills 4 in Basra, 35 hurt", "M. EAST"),
    (14, "Eisenkot invites Likud to coalition talks", "M. EAST"),
    (16, "MSF: 5,000 still missing in El-Fasher", "AFRICA"),
    (17, "Wembanyama scores 50, grabs 19 boards", "AMERICAS"),
    (18, "Nvidia faces SEC probe; shares fall 14%", "AMERICAS"),
    (19, "Bolsonaro stays in intensive care, stable", "AMERICAS"),
    (20, "Estonia to shut its Russia border on 1 Dec", "EUROPE"),
    (21, "South Korea minister quits in exam-leak scandal", "ASIA"),
    (22, "China bans US phones, calls them \u2018malicious\u2019", "ASIA"),
    (23, "Japan holds first live-fire drill with India", "ASIA"),
    (24, "Nepal\u2019s PM lands in Delhi on first visit", "ASIA"),
    (25, "Marles rejects US report on AUKUS subs", "OCEANIA"),
    (26, "EU and Indonesia sign trade deal; tariffs cut", "EUROPE"),
    (27, "Belgian air-traffic strike grounds Monday flights", "EUROPE"),
    (28, "France seeks UN action over Myanmar ruling", "EUROPE"),
    (29, "Chinese bomber turns back 170 km from Manila", "ASIA"),
    (30, "Liverpool host Man Utd 16:30 GMT, Pochettino debut", "EUROPE"),
    (31, "Zverev meets Alcaraz in ATP final 17:00 GMT", "EUROPE"),
    (32, "Saudi coalition downs three Houthi missiles", "M. EAST"),
    (33, "Four nations press Israel over Gaza aid", "M. EAST"),
    (34, "Australia chase 188 to beat England in 1st T20", "OCEANIA"),
    (35, "Drone attack hits five-storey block, Kyiv Oblast", "EUROPE"),
    (36, "Bitcoin rebounds above $60,000, up 1.85%", "GLOBAL"),
    (37, "Pope Leo hosts lunch for 1,300 poor guests", "EUROPE"),
    (38, "World court: Myanmar committed genocide", "ASIA"),
]

# region bar -- must sum to 38 (counted from panels + ALSO above)
REGIONS = [
    ("Europe", 12, REG_COL["Europe"]),
    ("M. East", 8, REG_COL["M. East"]),
    ("Asia", 7, REG_COL["Asia"]),
    ("Americas", 5, REG_COL["Americas"]),
    ("Africa", 2, REG_COL["Africa"]),
    ("Oceania", 3, REG_COL["Oceania"]),
    ("Global", 1, REG_COL["Global"]),
]

DATE_CHECK = (
    "Every story here happened, or was first reported, on Sunday 22 November "
    "2026 in at least one time zone. Tonight\u2019s barrage was 148 drones "
    "\u2014 not Friday\u2019s 400. Left out as earlier news: Peru quake "
    "(Fri 20 Nov) \u00b7 missiles landing in Poland (19 Nov) \u00b7 Kerch Bridge "
    "strikes (earlier this week) \u00b7 Shenzhen summit (19 Nov) \u00b7 Voyager 1 "
    "(18 Nov) \u00b7 GTA VI launch (19 Nov) \u00b7 Anthropic IPO (19 Nov). Not yet "
    "happened when drawn: final COP31 approval (06:00 GMT session) \u00b7 ATP "
    "final (17:00 GMT) \u00b7 Liverpool v Man Utd (16:30 GMT)."
)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, fnt, max_w):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, lines, fnt, fill=INK, leading=None):
    if leading is None:
        leading = fnt.size + 3
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def tag_chip(d, x, y, label, h=14, fsize=8):
    """Filled status tag; returns its width."""
    fnt = font(SANS_B, fsize)
    w = int(d.textlength(label, font=fnt)) + 12
    d.rounded_rectangle([x, y, x + w, y + h], radius=h // 2,
                        fill=TAG_COL[label])
    d.text((x + 6, y + 2), label, font=fnt, fill=(255, 255, 255))
    return w


# ---------------------------------------------------------------- world map
# Coarse but recognisable continent outlines, (lon, lat), equirectangular.
# Written from the atlas, not traced: real coastlines, simplified.
N_AMERICA = [(-168, 66), (-158, 58), (-148, 61), (-138, 59), (-130, 54),
             (-125, 49), (-124, 41), (-120, 34), (-112, 29), (-107, 24),
             (-102, 19), (-95, 16), (-89, 13), (-84, 10), (-79, 9),
             (-82, 14), (-86, 16), (-88, 21), (-91, 19), (-96, 19),
             (-97, 26), (-93, 30), (-88, 30), (-83, 30), (-81, 26),
             (-80, 32), (-76, 35), (-74, 40), (-70, 43), (-66, 45),
             (-60, 47), (-56, 50), (-61, 55), (-66, 58), (-71, 62),
             (-78, 62), (-86, 66), (-93, 66), (-100, 69), (-112, 68),
             (-126, 70), (-142, 70), (-156, 71), (-166, 68)]
GREENLAND = [(-55, 61), (-48, 60), (-41, 62), (-33, 68), (-23, 70),
             (-20, 75), (-28, 80), (-40, 81), (-55, 80), (-62, 76),
             (-66, 70), (-61, 65)]
S_AMERICA = [(-79, 9), (-77, 4), (-80, -3), (-81, -6), (-76, -12),
             (-72, -18), (-70, -24), (-70, -31), (-72, -38), (-73, -45),
             (-74, -51), (-69, -54), (-66, -55), (-67, -49), (-64, -43),
             (-61, -38), (-57, -34), (-51, -31), (-47, -27), (-40, -22),
             (-35, -9), (-35, -6), (-41, -3), (-44, -2), (-50, 0),
             (-53, 5), (-57, 6), (-61, 9), (-65, 11), (-71, 12), (-75, 10)]
AFRICA = [(-6, 35), (-10, 31), (-15, 27), (-17, 21), (-17, 15), (-15, 11),
          (-12, 8), (-8, 5), (-3, 5), (1, 6), (7, 4), (10, 4), (13, -1),
          (12, -6), (13, -11), (12, -17), (14, -23), (16, -28), (19, -34),
          (26, -34), (32, -29), (36, -24), (40, -16), (40, -11), (42, -4),
          (46, 0), (51, 2), (51, 11), (47, 11), (43, 12), (40, 15),
          (38, 18), (37, 22), (34, 27), (32, 31), (29, 31), (24, 32),
          (19, 32), (14, 32), (11, 34), (10, 37), (5, 37), (-1, 35)]
EURASIA = [(-9, 37), (-9, 43), (-2, 44), (-1, 46), (-4, 48), (0, 46),
           (3, 51), (6, 53), (8, 55), (8, 57), (11, 59), (6, 60), (6, 62),
           (11, 64), (14, 67), (20, 70), (28, 71), (34, 69), (42, 68),
           (50, 69), (58, 69), (66, 71), (73, 73), (80, 73), (88, 75),
           (98, 77), (108, 74), (118, 73), (128, 72), (138, 72),
           (148, 70), (157, 69), (162, 66), (170, 66), (178, 65),
           (178, 62), (170, 60), (162, 60), (158, 55), (156, 51),
           (150, 59), (142, 54), (140, 45), (135, 43), (130, 42),
           (127, 40), (126, 38), (121, 38), (120, 34), (122, 31),
           (120, 27), (117, 24), (110, 21), (108, 18), (105, 10),
           (103, 8), (100, 8), (98, 12), (94, 16), (92, 21), (89, 22),
           (86, 20), (82, 17), (80, 13), (77, 8), (75, 12), (72, 20),
           (68, 23), (66, 25), (62, 25), (58, 25), (56, 26), (54, 26),
           (52, 28), (50, 29), (48, 30), (49, 28), (51, 27), (54, 26),
           (57, 25), (59, 22), (55, 17), (52, 15), (48, 14), (45, 13),
           (43, 12), (40, 15), (39, 21), (37, 25), (35, 28), (34, 31),
           (36, 36), (33, 36), (30, 36), (27, 37), (23, 36), (22, 37),
           (19, 40), (15, 40), (12, 44), (8, 44), (3, 43), (0, 40),
           (-2, 37), (-6, 36)]
UK = [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (0, 53), (1, 51)]
IRELAND = [(-10, 52), (-8, 51), (-6, 52), (-6, 54), (-8, 55), (-10, 54)]
ICELAND = [(-22, 64), (-18, 63), (-14, 64), (-15, 66), (-20, 66), (-24, 65)]
JAPAN = [(130, 31), (132, 33), (134, 34), (137, 35), (139, 36), (140, 38),
         (141, 40), (142, 42), (144, 44), (141, 45), (140, 43), (137, 38),
         (133, 35)]
PHILIPPINES = [(120, 18), (122, 16), (121, 14), (122, 11), (120, 14)]
SUMATRA = [(95, 5), (100, 0), (104, -3), (106, -6), (103, -5), (98, 2)]
BORNEO = [(109, 1), (113, 4), (117, 6), (119, 2), (117, -2), (112, -3)]
JAVA = [(105, -6), (110, -7), (114, -8), (114, -7), (108, -6)]
NEW_GUINEA = [(131, -1), (136, -2), (141, -3), (146, -6), (147, -8),
              (141, -8), (136, -4)]
AUSTRALIA = [(114, -22), (114, -30), (115, -35), (118, -35), (124, -33),
             (129, -32), (132, -32), (136, -35), (138, -35), (140, -38),
             (145, -38), (150, -37), (153, -32), (153, -27), (150, -23),
             (146, -19), (142, -15), (142, -11), (137, -12), (135, -15),
             (132, -12), (130, -13), (126, -14), (122, -17), (118, -20)]
NEW_ZEALAND = [(167, -45), (170, -42), (174, -39), (176, -38), (178, -37),
               (175, -40), (172, -43), (168, -46)]
MADAGASCAR = [(44, -16), (47, -15), (50, -16), (49, -20), (45, -25),
              (43, -22)]
SRI_LANKA = [(80, 9), (81, 8), (81, 6), (80, 6)]

LAND_POLYS = [N_AMERICA, GREENLAND, S_AMERICA, AFRICA, EURASIA, UK,
              IRELAND, ICELAND, JAPAN, PHILIPPINES, SUMATRA, BORNEO, JAVA,
              NEW_GUINEA, AUSTRALIA, NEW_ZEALAND, MADAGASCAR, SRI_LANKA]

# map frame: lon -170..190, lat 74..-56
MAP = {"x0": 24, "x1": 1000, "y0": 556, "y1": 664}


def proj(lon, lat):
    x = MAP["x0"] + (lon + 170.0) / 360.0 * (MAP["x1"] - MAP["x0"])
    y = MAP["y0"] + (74.0 - lat) / 130.0 * (MAP["y1"] - MAP["y0"])
    return x, y


# (story num, lon, lat, dx, dy) -- dx/dy shift the numbered pin off the
# true dot so crowded Europe / Middle East pins do not overlap; a thin
# leader line joins dot to pin. BepiColombo (13) is pinned at Darmstadt,
# where ESA flies it from -- a Mercury probe has no Earth coastline.
PINS = [
    (1, 30.7, 36.9, -15, -12),   # Antalya
    (2, 33.4, 47.9, 17, -11),    # Kryvyi Rih
    (3, 50.6, 26.2, 0, 13),      # Bahrain
    (4, 24.8, 60.0, -2, -12),    # Gulf of Finland
    (5, 114.2, 22.3, 0, 0),      # Hong Kong
    (6, 56.3, 26.6, 17, -2),     # Hormuz
    (7, 174.8, -41.3, 0, 0),     # Wellington
    (8, -115.1, 36.2, 0, 0),     # Las Vegas
    (9, 51.4, 35.7, 13, -12),    # Tehran
    (10, 34.5, 31.5, -15, 12),   # Gaza
    (11, -107.4, 24.8, 0, 0),    # Sinaloa
    (12, 6.3, 4.8, 0, 0),        # Bayelsa
    (13, 8.65, 49.87, -15, 8),   # Darmstadt (ESA control)
]


# ---------------------------------------------------------------- scenes
def scene_cop31(d, x0, y0, x1, y1):
    """COP31 plenary: sand hall, stage with podium and flags, big 06:00
    clock, arcs of delegate heads."""
    d.rectangle([x0, y0, x1, y1], fill=(233, 214, 168))
    d.rectangle([x0, y0, x1, y0 + 12], fill=(196, 164, 110))
    # stage: podium + flags row
    d.rectangle([x0 + 12, y0 + 22, x0 + 118, y0 + 34], fill=(120, 84, 50))
    d.polygon([(x0 + 60, y0 + 34), (x0 + 70, y0 + 34), (x0 + 65, y0 + 46)],
              fill=(90, 60, 36))
    for i, col in enumerate([(178, 34, 28), (46, 95, 138), (62, 122, 78),
                             (192, 138, 26), (122, 92, 158)]):
        fx = x0 + 132 + i * 26
        d.line([fx, y0 + 14, fx, y0 + 32], fill=INK, width=2)
        d.rectangle([fx, y0 + 14, fx + 18, y0 + 24], fill=col)
    # big clock, hands at 6 o'clock, top-right
    cx, cy, r = x1 - 30, y0 + 26, 17
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 252, 244),
              outline=INK, width=2)
    d.line([cx, cy, cx, cy - r + 4], fill=INK, width=2)
    d.line([cx, cy, cx, cy + r - 5], fill=RED, width=2)
    d.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=INK)
    # delegate arcs: three rows of heads
    for row in range(3):
        yy = y0 + 40 + row * 6
        for i in range(14):
            xx = x0 + 14 + i * 21
            col = (70, 60, 90) if (i + row) % 3 == 0 else (
                (150, 60, 50) if (i + row) % 3 == 1 else (60, 110, 80))
            d.ellipse([xx, yy, xx + 8, yy + 8], fill=col)


def scene_ukraine(d, x0, y0, x1, y1):
    """Kyiv night: dark sky, drone dots with light trails, orange blasts
    over the skyline, one searchlight beam."""
    d.rectangle([x0, y0, x1, y1], fill=(16, 24, 48))
    for sx, sy in [(x0 + 24, y0 + 6), (x0 + 70, y0 + 4), (x1 - 40, y0 + 7),
                   (x0 + 170, y0 + 5), (x1 - 110, y0 + 9)]:
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(220, 220, 200))
    # searchlight beam from the right
    d.polygon([(x1 - 60, y1), (x1 - 30, y1), (x0 + 210, y0 + 8),
               (x0 + 190, y0 + 8)], fill=(60, 70, 110))
    # skyline silhouettes with lit windows
    for bx, bw, bh in [(x0 + 8, 34, 26), (x0 + 46, 26, 32), (x0 + 76, 40, 22),
                       (x0 + 120, 30, 28), (x0 + 154, 36, 24),
                       (x1 - 88, 30, 30), (x1 - 52, 42, 20)]:
        d.rectangle([bx, y1 - bh, bx + bw, y1], fill=(8, 12, 26))
        for wy in range(y1 - bh + 4, y1 - 4, 7):
            for wx in range(bx + 4, bx + bw - 4, 8):
                if (wx + wy) % 3 == 0:
                    d.rectangle([wx, wy, wx + 2, wy + 3], fill=(255, 210, 90))
    # explosion bursts
    for ex, ey, er in [(x0 + 96, y0 + 26, 12), (x0 + 200, y0 + 20, 10),
                       (x1 - 70, y0 + 28, 9)]:
        d.ellipse([ex - er, ey - er, ex + er, ey + er], fill=(255, 140, 30))
        d.ellipse([ex - er // 2, ey - er // 2, ex + er // 2, ey + er // 2],
                  fill=(255, 220, 120))
    # drones: small dark dots with white trails
    for dx, dy, dl in [(x0 + 60, y0 + 12, 18), (x0 + 140, y0 + 9, 14),
                       (x0 + 230, y0 + 14, 16), (x1 - 30, y0 + 11, 12)]:
        d.line([dx - dl, dy, dx, dy], fill=(220, 220, 200), width=1)
        d.ellipse([dx - 2, dy - 2, dx + 2, dy + 2], fill=(30, 30, 30),
                  outline=(220, 220, 200), width=1)


def scene_bahrain(d, x0, y0, x1, y1):
    """Bahrain night: refinery towers, one industrial site ablaze, smoke
    drifting, a low moon."""
    d.rectangle([x0, y0, x1, y1], fill=(18, 28, 52))
    d.ellipse([x0 + 18, y0 + 6, x0 + 34, y0 + 22], fill=(235, 230, 200))
    for sx, sy in [(x0 + 80, y0 + 5), (x0 + 150, y0 + 8), (x1 - 50, y0 + 6),
                   (x1 - 120, y0 + 4)]:
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(220, 220, 200))
    # refinery blocks and stacks
    d.rectangle([x0 + 8, y0 + 30, x0 + 52, y1], fill=(10, 14, 28))
    d.rectangle([x1 - 96, y0 + 32, x1 - 56, y1], fill=(10, 14, 28))
    d.rectangle([x1 - 48, y0 + 28, x1 - 8, y1], fill=(12, 16, 32))
    for tx in (x0 + 20, x0 + 40, x1 - 80, x1 - 30):
        d.rectangle([tx, y0 + 14, tx + 6, y0 + 32], fill=(10, 14, 28))
    # round storage tanks
    for tx in (x0 + 66, x0 + 96):
        d.ellipse([tx, y0 + 34, tx + 26, y1], fill=(14, 18, 34))
    # central fire, taller than the rest
    for fx, fh, col in [(x0 + 150, 34, (255, 120, 20)),
                        (x0 + 180, 26, (255, 170, 30)),
                        (x0 + 208, 30, (255, 200, 60))]:
        d.polygon([(fx - 13, y1), (fx, y1 - fh), (fx + 13, y1)], fill=col)
        d.polygon([(fx - 5, y1), (fx, y1 - fh + 11), (fx + 5, y1)],
                  fill=(255, 230, 120))
    # smoke
    for sx, sy, sr in [(x0 + 165, y0 + 6, 10), (x0 + 200, y0 + 4, 12),
                       (x0 + 235, y0 + 8, 8)]:
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(90, 90, 100))


SCENES = {"cop31": scene_cop31, "ukraine": scene_ukraine,
          "bahrain": scene_bahrain}


# ---------------------------------------------------------------- panels
def draw_hero(d, box, story):
    num, kicker, title, body, region, tag, kind = story
    x0, y0, x1, y1 = box
    accent = REG_COL[region]
    d.rectangle(box, fill=PANEL_BG, outline=LINE, width=1)
    d.rectangle([x0, y0, x1, y0 + 3], fill=accent)
    SCENES[kind](d, x0 + 1, y0 + 4, x1 - 1, y0 + 56)
    d.ellipse([x0 + 7, y0 + 9, x0 + 31, y0 + 33], fill=RED,
              outline=(255, 255, 255), width=1)
    nb = font(SANS_B, 14)
    tw = d.textlength(str(num), font=nb)
    d.text((x0 + 19 - tw / 2, y0 + 11), str(num), font=nb, fill=(255, 255, 255))
    d.text((x0 + 8, y0 + 59), kicker, font=font(SANS_B, 9), fill=accent)
    tag_chip(d, x1 - 72, y0 + 58, tag)
    tf = font(SERIF_B, 15)
    lines = wrap(d, title, tf, x1 - x0 - 16)
    assert len(lines) <= 2, f"hero {num} title too long: {lines}"
    text_block(d, x0 + 8, y0 + 74, lines, tf, leading=16)
    bf = font(SANS, 11)
    blines = wrap(d, body, bf, x1 - x0 - 16)
    assert len(blines) <= 2, f"hero {num} body too long: {blines}"
    text_block(d, x0 + 8, y0 + 74 + 16 * len(lines) + 2, blines, bf,
               fill=(60, 55, 48), leading=12)


def draw_small(d, box, story):
    num, kicker, title, body, region, tag = story
    x0, y0, x1, y1 = box
    accent = REG_COL[region]
    d.rectangle(box, fill=PANEL_BG, outline=LINE, width=1)
    d.rectangle([x0, y0, x1, y0 + 3], fill=accent)
    d.ellipse([x0 + 6, y0 + 8, x0 + 26, y0 + 28], fill=RED,
              outline=(255, 255, 255), width=1)
    nb = font(SANS_B, 11)
    tw = d.textlength(str(num), font=nb)
    d.text((x0 + 16 - tw / 2, y0 + 10), str(num), font=nb, fill=(255, 255, 255))
    d.text((x0 + 31, y0 + 11), kicker, font=font(SANS_B, 8), fill=accent)
    tag_chip(d, x1 - 66, y0 + 8, tag, h=13, fsize=7)
    tf = font(SERIF_B, 12)
    lines = wrap(d, title, tf, x1 - x0 - 16)
    assert len(lines) <= 2, f"panel {num} title too long: {lines}"
    text_block(d, x0 + 8, y0 + 32, lines, tf, leading=14)
    bf = font(SANS, 10)
    blines = wrap(d, body, bf, x1 - x0 - 16)
    assert len(blines) <= 2, f"panel {num} body too long: {blines}"
    text_block(d, x0 + 8, y0 + 32 + 14 * len(lines) + 3, blines, bf,
               fill=(60, 55, 48), leading=12)
    d.text((x0 + 8, y0 + 84), region.upper(), font=font(SANS_B, 8),
           fill=accent)


# ---------------------------------------------------------------- page
def main():
    assert sum(n for _, n, _ in REGIONS) == 38, "region bar must total 38"
    assert len(HEROES) + len(PANELS) == 13, "must be 13 panels"
    assert len(ALSO) == 25, "ALSO must be 25 stories"
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([10, 10, W - 11, H - 11], fill=PAPER, outline=INK, width=2)

    # ---- masthead
    mf = font(SERIF_B, 40)
    t = "THE WORLD IN ONE DAY"
    d.text(((W - d.textlength(t, font=mf)) / 2, 16), t, font=mf, fill=RED)
    d.line([24, 60, W - 24, 60], fill=INK, width=2)
    d.line([24, 64, W - 24, 64], fill=INK, width=1)

    # ---- date title + subhead
    tf = font(SERIF_B, 36)
    t = "Sunday 22 November 2026"
    d.text(((W - d.textlength(t, font=tf)) / 2, 70), t, font=tf, fill=INK)
    sf = font(SANS, 13)
    t = ("COP31 nears a deal \u00b7 148 drones over Ukraine \u00b7 "
         "Iran strikes US bases in Bahrain")
    d.text(((W - d.textlength(t, font=sf)) / 2, 112), t, font=sf, fill=GREY)

    # ---- tag legend (the TAGGED signature)
    y = 132
    d.text((24, y), "TAGGED:", font=font(SANS_B, 11), fill=INK)
    x = 24 + d.textlength("TAGGED: ", font=font(SANS_B, 11))
    for label, note in [("ONGOING", "still unfolding"),
                        ("REPORTED", "confirmed"),
                        ("CLAIM", "one side says so")]:
        x += tag_chip(d, int(x), y, label) + 5
        nf = font(SANS, 10)
        d.text((x, y + 1), note, font=nf, fill=GREY)
        x += d.textlength(note, font=nf) + 18
    d.text((W - 24 - d.textlength("38 STORIES \u00b7 22 NOV 2026",
                                  font=font(SANS_B, 11)), y),
           "38 STORIES \u00b7 22 NOV 2026", font=font(SANS_B, 11), fill=INK)

    # ---- stat strip: 6 boxes
    y = 150
    bw = (W - 48 - 5 * 6) // 6
    for i, (num, label) in enumerate(STATS):
        x0 = 24 + i * (bw + 6)
        d.rectangle([x0, y, x0 + bw, y + 40], fill=(255, 252, 244),
                    outline=LINE, width=1)
        nf = font(SERIF_B, 21)
        d.text((x0 + (bw - d.textlength(num, font=nf)) / 2, y + 2), num,
               font=nf, fill=RED)
        lf = font(SANS_B, 8)
        d.text((x0 + (bw - d.textlength(label, font=lf)) / 2, y + 27), label,
               font=lf, fill=GREY)

    # ---- hero row: #1 COP31, #2 Ukraine-148, #3 Bahrain
    y = 196
    hw = (W - 48 - 2 * 8) // 3
    for i, st in enumerate(HEROES):
        x0 = 24 + i * (hw + 8)
        draw_hero(d, (x0, y, x0 + hw, y + 126), st)

    # ---- small rows: panels 4-13, 5 per row
    sw = (W - 48 - 4 * 6) // 5
    for r in range(2):
        y = 328 + r * 104
        for c in range(5):
            st = PANELS[r * 5 + c]
            x0 = 24 + c * (sw + 6)
            draw_small(d, (x0, y, x0 + sw, y + 98), st)

    # ---- map + region legend
    y = 536
    d.text((24, y), "WHERE IT HAPPENED \u2014 13 STORIES PINNED",
           font=font(SANS_B, 13), fill=INK)
    legend = ("STORIES BY REGION \u2014 38: Europe 12 \u00b7 M. East 8 \u00b7 "
              "Asia 7 \u00b7 Americas 5 \u00b7 Africa 2 \u00b7 Oceania 3 \u00b7 "
              "Global 1")
    lf = font(SANS_B, 10)
    d.text((W - 24 - d.textlength(legend, font=lf), y + 2), legend, font=lf,
           fill=INK)
    my0, my1 = MAP["y0"], MAP["y1"]
    d.rectangle([MAP["x0"], my0, MAP["x1"], my1], fill=MAP_BG, outline=LINE,
                width=1)
    for lon in range(-150, 181, 30):
        gx, _ = proj(lon, 74)
        d.line([gx, my0, gx, my1], fill=(226, 221, 205), width=1)
    for lat in (60, 30, 0, -30):
        _, gy = proj(0, lat)
        d.line([MAP["x0"], gy, MAP["x1"], gy], fill=(226, 221, 205), width=1)
    for poly in LAND_POLYS:
        pts = [proj(lon, lat) for lon, lat in poly]
        d.polygon(pts, fill=LAND, outline=LAND_LINE)
    labf = font(SANS_B, 8)
    for label, lon, lat in [("NORTH AMERICA", -100, 52),
                            ("SOUTH AMERICA", -60, -14),
                            ("EUROPE", 14, 58),
                            ("AFRICA", 18, 2),
                            ("ASIA", 88, 50),
                            ("OCEANIA", 138, -26)]:
        lx, ly = proj(lon, lat)
        d.text((lx - d.textlength(label, font=labf) / 2, ly), label,
               font=labf, fill=GREY)
    pf = font(SANS_B, 10)
    for num, lon, lat, dx, dy in PINS:
        px, py = proj(lon, lat)
        cx, cy = px + dx, py + dy
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=INK)
        if dx or dy:
            d.line([px, py, cx, cy], fill=INK, width=1)
        d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=RED,
                  outline=(255, 255, 255), width=1)
        tw = d.textlength(str(num), font=pf)
        d.text((cx - tw / 2, cy - 7), str(num), font=pf, fill=(255, 255, 255))

    # ---- region bar (full width, segments proportional to counts)
    by = 670
    x = 24
    for name, n, col in REGIONS:
        wseg = int((W - 48) * n / 38)
        if wseg:
            d.rectangle([x, by, x + wseg - 1, by + 18], fill=col)
        x += wseg
    d.rectangle([24, by, W - 24, by + 18], outline=INK, width=1)
    bf = font(SANS_B, 8)
    x = 24
    for name, n, col in REGIONS:
        wseg = int((W - 48) * n / 38)
        lab = f"{name.upper()} {n}"
        if wseg > d.textlength(lab, font=bf) + 8:
            d.text((x + 5, by + 5), lab, font=bf, fill=(255, 255, 255))
        x += wseg

    # ---- ALSO list, 2 columns, region tag per line
    y = 694
    d.text((24, y), "ALSO ON SUNDAY 22 NOVEMBER \u2014 25 MORE STORIES",
           font=font(SANS_B, 13), fill=INK)
    d.line([24, y + 18, W - 24, y + 18], fill=INK, width=1)
    af = font(SANS, 11)
    ab = font(SANS_B, 11)
    rf = font(SANS_B, 8)
    ay = y + 24
    col_w = 480
    for idx, (num, title, reg) in enumerate(ALSO):
        col = idx // 13
        row = idx % 13
        x0 = 24 + col * 488
        yy = ay + row * 14
        d.text((x0, yy), f"{num}.", font=ab, fill=RED)
        tw = d.textlength(title, font=af)
        assert tw <= col_w - 30 - d.textlength(reg, font=rf) - 8, (
            f"ALSO {num} too long: {title}")
        d.text((x0 + 26, yy), title, font=af, fill=INK)
        rw = d.textlength(reg, font=rf)
        d.text((x0 + col_w - rw, yy + 1), reg, font=rf, fill=GREY)

    # ---- DATE CHECK (red box)
    y = 904
    d.rectangle([24, y, W - 24, y + 62], fill=(255, 240, 236), outline=RED,
                width=2)
    d.text((34, y + 4), "DATE CHECK \u2014 NOT 22 NOVEMBER:",
           font=font(SANS_B, 11), fill=RED)
    df = font(SANS, 10)
    lines = wrap(d, DATE_CHECK, df, W - 48 - 20)
    assert len(lines) <= 4, f"DATE CHECK too long: {len(lines)} lines"
    text_block(d, 34, y + 19, lines, df, leading=11)

    # ---- footer
    y = 972
    ff = font(SANS_B, 10)
    t = ("Every story here happened, or was first reported, on Sunday "
         "22 November 2026.")
    d.text(((W - d.textlength(t, font=ff)) / 2, y), t, font=ff, fill=INK)
    sf2 = font(SANS, 9)
    t = ("Sources: Reuters \u00b7 AP \u00b7 AFP \u00b7 BBC \u00b7 SCMP \u00b7 "
         "ESPNcricinfo \u00b7 ESA \u00b7 MSF \u00b7 Vatican News \u00b7 Guardian")
    d.text(((W - d.textlength(t, font=sf2)) / 2, y + 12), t, font=sf2,
           fill=GREY)
    t = ("HOW WE CHECKED: each story dated to Sunday 22 November 2026 in "
         "wire and official reports; earlier stories kept out of the grid.")
    d.text(((W - d.textlength(t, font=sf2)) / 2, y + 23), t, font=sf2,
           fill=GREY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img_q = img.convert("P", palette=Image.ADAPTIVE, colors=256)
    img_q.save(out, "PNG", optimize=True)
    print(out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
