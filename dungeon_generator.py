
"""
Dungeon Generator v1.0
Retro Matt RPG Helper Suite
Generates a simple random ASCII dungeon.
"""

import random

WIDTH = 20
HEIGHT = 12

TILES = {
    "wall": "#",
    "floor": ".",
    "treasure": "$",
    "monster": "M",
    "stairs": ">"
}

def create_dungeon():
    dungeon = [[TILES["wall"] for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Carve random rooms
    for _ in range(90):
        x = random.randint(1, WIDTH - 2)
        y = random.randint(1, HEIGHT - 2)
        dungeon[y][x] = TILES["floor"]

    # Place special tiles
    def place(tile):
        while True:
            x = random.randint(1, WIDTH - 2)
            y = random.randint(1, HEIGHT - 2)
            if dungeon[y][x] == TILES["floor"]:
                dungeon[y][x] = tile
                break

    for _ in range(3):
        place(TILES["treasure"])

    for _ in range(5):
        place(TILES["monster"])

    place(TILES["stairs"])

    return dungeon

def print_dungeon(dungeon):
    print("\n=== RANDOM DUNGEON ===\n")
    for row in dungeon:
        print("".join(row))
    print("\nLegend")
    print("# = Wall")
    print(". = Floor")
    print("$ = Treasure")
    print("M = Monster")
    print("> = Exit")

while True:
    print("\n=== DUNGEON GENERATOR ===")
    print("1. Generate Dungeon")
    print("2. Save Dungeon")
    print("3. Quit")

    choice = input("> ")

    if choice == "1":
        current = create_dungeon()
        print_dungeon(current)

    elif choice == "2":
        try:
            current
        except NameError:
            print("Generate a dungeon first.")
            continue

        with open("dungeon_map.txt", "w") as f:
            for row in current:
                f.write("".join(row) + "\n")
        print("Dungeon saved as dungeon_map.txt")

    elif choice == "3":
        break
