
"""
Loot Generator v1.0
Retro Matt RPG Helper Suite
"""

import random

WEAPONS = [
    "Iron Sword", "Steel Axe", "Oak Bow", "War Hammer",
    "Magic Staff", "Dagger", "Spear", "Crossbow"
]

ARMOR = [
    "Leather Armor", "Chainmail", "Plate Armor",
    "Wizard Robe", "Shield", "Helmet"
]

POTIONS = [
    "Health Potion", "Mana Potion", "Stamina Potion",
    "Antidote", "Elixir"
]

TREASURE = [
    "Gold Coins", "Silver Coins", "Gemstone",
    "Ancient Relic", "Magic Ring", "Treasure Map"
]

RARITY = {
    "Common": 50,
    "Uncommon": 25,
    "Rare": 15,
    "Epic": 8,
    "Legendary": 2
}

def random_rarity():
    roll = random.randint(1,100)
    total = 0
    for rarity, chance in RARITY.items():
        total += chance
        if roll <= total:
            return rarity
    return "Common"

def generate_loot():
    category = random.choice(["Weapon","Armor","Potion","Treasure"])

    if category == "Weapon":
        item = random.choice(WEAPONS)
    elif category == "Armor":
        item = random.choice(ARMOR)
    elif category == "Potion":
        item = random.choice(POTIONS)
    else:
        item = random.choice(TREASURE)

    rarity = random_rarity()
    value = random.randint(5,250) * (["Common","Uncommon","Rare","Epic","Legendary"].index(rarity)+1)

    print("\n========== LOOT ==========")
    print("Category :", category)
    print("Item     :", item)
    print("Rarity   :", rarity)
    print("Value    :", value, "gold")
    print("==========================")

while True:
    print("\n=== LOOT GENERATOR ===")
    print("1. Generate Loot")
    print("2. Generate Treasure Chest (5 Items)")
    print("3. Quit")

    choice = input("> ")

    if choice == "1":
        generate_loot()

    elif choice == "2":
        print("\n===== TREASURE CHEST =====")
        for i in range(5):
            generate_loot()

    elif choice == "3":
        break
