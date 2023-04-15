import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total_sum = 0
number_of_dice = 0
print()
print(" *** Program will roll the dice and display the result. ***")


while True:
  try:
     number_of_dice = int(input("\nNumber of dice? [ (1-6) or enter 7 to quit ]: "))       
  except ValueError:
     print("\nInvalid input. Only numbers between 1 and 7 are allowed.")
     continue
  else:

    if number_of_dice >0 and number_of_dice <= 6:


        for die in range(number_of_dice):
            dice.append(random.randint(1, 6))


        for line in range(5):
            for die in dice:
                print(dice_art.get(die)[line], end="")
            print()

        for die in dice:
            total_sum += die
        print(f"Total sum : {total_sum}\n")
        print("BYE !!!!")
        break

    elif number_of_dice == 7:
        print()
        print("BYE !!!!")
        break

    else:
        print("\n (1-6 Please)")

    

    
