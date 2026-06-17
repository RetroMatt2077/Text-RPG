
"""
NPC Generator v1.0
Retro Matt RPG Helper Suite
"""

import random
import json

FIRST_NAMES = [
    "Alden","Luna","Thorin","Elara","Cedric","Rowan","Kael",
    "Mira","Borin","Sylvia","Darius","Nessa","Garrick","Faye"
]

LAST_NAMES = [
    "Ironwood","Stormborn","Blackstone","Rivers","Oakheart",
    "Silverleaf","Ashwalker","Brightblade","Hillcrest","Dawnstar"
]

RACES = ["Human","Elf","Dwarf","Halfling","Orc","Tiefling","Dragonborn"]
JOBS = [
    "Blacksmith","Merchant","Innkeeper","Guard","Farmer",
    "Hunter","Mage","Priest","Bard","Thief","Scholar","Alchemist"
]

PERSONALITIES = [
    "Friendly","Gruff","Cheerful","Suspicious","Wise",
    "Cowardly","Brave","Greedy","Honest","Mysterious"
]

QUIRKS = [
    "Always whistles","Loves cats","Afraid of magic",
    "Collects shiny rocks","Never removes helmet",
    "Talks to themselves","Has a pet raven",
    "Laughs loudly","Speaks in riddles","Obsessed with treasure"
]

def generate_npc():
    npc = {
        "Name": random.choice(FIRST_NAMES) + " " + random.choice(LAST_NAMES),
        "Race": random.choice(RACES),
        "Occupation": random.choice(JOBS),
        "Age": random.randint(18,80),
        "Personality": random.choice(PERSONALITIES),
        "Quirk": random.choice(QUIRKS),
        "Gold": random.randint(0,100)
    }
    return npc

while True:
    print("\n=== NPC GENERATOR ===")
    print("1. Generate NPC")
    print("2. Generate Village (10 NPCs)")
    print("3. Quit")

    choice = input("> ")

    if choice == "1":
        npc = generate_npc()
        print("\n===== NPC =====")
        for k,v in npc.items():
            print(f"{k}: {v}")

        if input("\nSave NPC? (y/n): ").lower()=="y":
            fn = npc["Name"].replace(" ","_") + ".json"
            with open(fn,"w") as f:
                json.dump(npc,f,indent=4)
            print("Saved as",fn)

    elif choice == "2":
        village=[]
        print("\n===== VILLAGE =====")
        for i in range(10):
            npc=generate_npc()
            village.append(npc)
            print(f'{i+1}. {npc["Name"]} - {npc["Occupation"]} ({npc["Race"]})')

        if input("\nSave village? (y/n): ").lower()=="y":
            with open("village_npcs.json","w") as f:
                json.dump(village,f,indent=4)
            print("Village saved.")

    elif choice=="3":
        break
