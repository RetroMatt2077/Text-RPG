
"""
Character Creator Deluxe v2.0
"""

import random
import json

RACES=["Human","Elf","Dwarf","Halfling","Orc","Tiefling","Dragonborn"]
CLASSES=["Fighter","Wizard","Rogue","Cleric","Ranger","Paladin","Barbarian"]
BACKGROUNDS=["Soldier","Scholar","Outlander","Noble","Criminal","Hermit","Merchant"]
ALIGNMENTS=["LG","NG","CG","LN","N","CN","LE","NE","CE"]
STATS=["STR","DEX","CON","INT","WIS","CHA"]

def roll_stat():
    rolls=sorted([random.randint(1,6) for _ in range(4)])
    return sum(rolls[1:])

def modifier(score):
    return (score-10)//2

while True:
    print("\n=== CHARACTER CREATOR DELUXE ===")
    name=input("Name: ")
    race=input(f"Race {RACES}: ") or random.choice(RACES)
    cls=input(f"Class {CLASSES}: ") or random.choice(CLASSES)

    stats={s:roll_stat() for s in STATS}

    hp=10+modifier(stats["CON"])
    ac=10+modifier(stats["DEX"])
    gold=random.randint(10,100)
    bg=random.choice(BACKGROUNDS)
    align=random.choice(ALIGNMENTS)

    equipment={
        "Fighter":["Sword","Shield","Chain Armor"],
        "Wizard":["Spellbook","Staff","Robes"],
        "Rogue":["Daggers","Leather Armor","Lockpicks"],
        "Cleric":["Mace","Holy Symbol"],
        "Ranger":["Bow","Sword"],
        "Paladin":["Longsword","Shield"],
        "Barbarian":["Greataxe","Furs"]
    }.get(cls,["Backpack"])

    char={
        "Name":name,
        "Race":race,
        "Class":cls,
        "Background":bg,
        "Alignment":align,
        "Gold":gold,
        "HP":hp,
        "AC":ac,
        "Stats":stats,
        "Equipment":equipment
    }

    print("\n===== CHARACTER SHEET =====")
    for k,v in char.items():
        if k!="Stats":
            print(f"{k}: {v}")
    print("\nStats")
    for s,val in stats.items():
        print(f"{s}: {val} ({modifier(val):+})")

    if input("\nSave JSON? y/n: ").lower()=="y":
        fn=name.replace(" ","_")+".json"
        with open(fn,"w") as f:
            json.dump(char,f,indent=4)
        print("Saved",fn)

    if input("\nAnother character? y/n: ").lower()!="y":
        break
