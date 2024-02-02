import random

def roll2Dice(): # function that rolls 2 dice and outputs the result
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2

    print(f"{dice1}, {dice2} (sum: {sum})")
    return sum

def menu(): # function to print menu text
    print("DICE ROLL SIMULATOR MENU")
    print("1. Roll Dice Once")
    print("2. Roll Dice 5 Times")
    print("3. Roll Dice 'n' Times")
    print("4. Roll Dice Until Snake Eyes")
    print("5. Exit")

menu()

inp = int(input("Select an option (1-5):"))
while(inp != 5): # keep displaying the menu until the user chooses 5
    print("\n")
    match inp:
        case 1:
            roll2Dice()
        case 2:
            for i in range(5):
                roll2Dice()
        case 3:
            numOfRolls = int(input("How many rolls would you like?"))
            for i in range(numOfRolls):
                roll2Dice()
        case 4:
            sum = 0
            numOfRolls = 0
            while(sum != 2):
                sum = roll2Dice()
                numOfRolls += 1
            print(f"SNAKE EYES! It took {numOfRolls} rolls to get snake eyes.")

    menu()
    inp = int(input("Select an option (1-5):"))
