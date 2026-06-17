
"""
Dice Roller Deluxe v2.0
Author: Retro Matt / ChatGPT

Features
- Dice notation parser (2d6+3, d20, 4d8-2)
- Advantage / Disadvantage
- Critical hit/fumble detection
- Roll history
- Save history to file
"""

import random
import re

history=[]

def roll_die(s):
    return random.randint(1,s)

def parse(notation):
    m=re.fullmatch(r'(\d*)d(\d+)([+-]\d+)?',notation.replace(" ","").lower())
    if not m:
        return None
    count=int(m.group(1) or 1)
    sides=int(m.group(2))
    mod=int(m.group(3) or 0)
    return count,sides,mod

while True:
    print("\n"+"="*50)
    print("      DICE ROLLER DELUXE v2.0")
    print("="*50)
    print("1) Roll Dice Notation")
    print("2) Advantage (d20)")
    print("3) Disadvantage (d20)")
    print("4) View History")
    print("5) Save History")
    print("6) Quit")

    c=input("\nChoice: ")

    if c=="6":
        break

    elif c=="1":
        text=input("Enter notation (ex: 4d6+2): ")
        parsed=parse(text)
        if not parsed:
            print("Invalid notation.")
            continue
        count,sides,mod=parsed
        rolls=[roll_die(sides) for _ in range(count)]
        total=sum(rolls)+mod
        print(f"Rolls : {rolls}")
        if mod:
            print(f"Modifier: {mod:+}")
        print(f"Total : {total}")

        if sides==20 and count==1:
            if rolls[0]==20:
                print("*** CRITICAL HIT! ***")
            elif rolls[0]==1:
                print("*** CRITICAL FAIL! ***")

        history.append(f"{text} -> {rolls} {mod:+} = {total}")

    elif c=="2":
        a,b=roll_die(20),roll_die(20)
        print(f"{a}, {b} -> {max(a,b)}")
        history.append(f"ADV {a},{b}->{max(a,b)}")

    elif c=="3":
        a,b=roll_die(20),roll_die(20)
        print(f"{a}, {b} -> {min(a,b)}")
        history.append(f"DIS {a},{b}->{min(a,b)}")

    elif c=="4":
        if not history:
            print("No history.")
        else:
            print("\n".join(history))

    elif c=="5":
        with open("dice_history.txt","w") as f:
            for h in history:
                f.write(h+"\n")
        print("History saved to dice_history.txt")
