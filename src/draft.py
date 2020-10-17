import random

def pairs():
  codes = list(cards().keys())
  random.shuffle(codes) 
  p1 = []
  p2 = []

  for i in range(4):
    p1.append((codes.pop(), codes.pop()))
    p2.append((codes.pop(), codes.pop()))
  return (p1, p2)

def get_name(num):
  return cards()[num]

def cards():
  return {
    26000000: "Knight",
    26000001: "Archers",
    26000002: "Goblins",
    26000003: "Giant",
    26000004: "Pekka",
    26000005: "Minions",
    26000006: "Balloon",
    26000007: "Whitch",
    26000008: "Barbarians",
    26000009: "Golem",
    26000010: "Skeletons",
    26000011: "Valkyrie",
    26000012: "Skeleton Army",
    26000013: "Bomber",
    26000014: "Musketeer",
    26000015: "Baby Dragon",
    26000016: "Prince",
    26000017: "Wizard",
    26000018: "Mini Pekka",
    26000019: "Spear Goblins",
    26000020: "Giant Skeleton",
    26000021: "Hog Rider",
    26000022: "Minion Horde",
    26000023: "Ice Wizard",
    26000024: "Royal Giant",
    26000025: "Guards",
    26000026: "Princess",
    26000027:	"Dark Prince",
    26000028: "Three Musketeers",
    26000029: "Lava Hound",
    26000030: "Ice Spirit",
    26000031: "Fire Spirits",
    26000032: "Miner",
    26000033: "Sparky",
    26000034: "Bowler",
    26000035: "Lumberjack",
    26000036: "Battle Ram",
    26000037: "Inferno Dragon",
    26000038: "Ice Golem",
    26000039: "Mega Minion",
    26000040: "Dart Goblin",
    26000041: "Goblin Gang",
    26000042: "Electro Wizard",
    26000043: "Elite Barbarians",
    26000044: "Hunter",
    26000045: "Executioner",
    26000046: "Bandit",

    26000048: "Night Witch",
    26000049: "Bats",
    26000050: "Royal Ghost",

    26000052: "Zappies",


    27000000: "Canon",
    27000001: "Goblin Hut",
    27000002: "Mortar",
    27000003: "Inferno Tower",
    27000004: "Bomb Tower",
    27000005: "Barbarian Hut",
    27000006: "Tesla",
    27000007: "Elixir Collector",
    27000008: "X-Bow",
    27000009: "Tombstone",
    27000010: "Furnace",


    28000000: "Fireball",
    28000001: "Arrows",
    28000002: "Rage",
    28000003: "Rocket",
    28000004: "Goblin Barrel",
    28000005: "Freeze",
    28000006: "Mirror",
    28000007: "Lighning",
    28000008: "Zap",
    28000009: "Poison",
    28000010: "Graveyard",
    28000011: "Log",
    28000012: "Tornado",
    28000013: "Clone",

    28000016: "Heal"
  }

