"""
Calculator Deluxe
Author: Retro Matt

Features:
- Addition
- Subtraction
- Multiplication
- Division
- Exponents
- Square Root
- Modulus
- Continuous calculations
"""

import math

def menu():
    print("\n" + "=" * 40)
    print("        CALCULATOR DELUXE")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Modulus (%)")
    print("8. Quit")

while True:
    menu()
    choice = input("\nSelect an option (1-8): ").strip()

    if choice == "8":
        print("\nThanks for using Calculator Deluxe!")
        break

    try:
        if choice == "6":
            num = float(input("Enter a number: "))
            if num < 0:
                print("Cannot take square root of a negative number.")
            else:
                print(f"√{num} = {math.sqrt(num)}")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print(f"Result: {a + b}")
        elif choice == "2":
            print(f"Result: {a - b}")
        elif choice == "3":
            print(f"Result: {a * b}")
        elif choice == "4":
            if b == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {a / b}")
        elif choice == "5":
            print(f"Result: {a ** b}")
        elif choice == "7":
            if b == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {a % b}")
        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter valid numbers.")
