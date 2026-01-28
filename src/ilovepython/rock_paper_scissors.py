import random

options = ("rock", "paper", "scissors")

start = input("press e to start the game, q to quit: ")
print()
choice = ""
count = 0

while start == "e" and choice != "q":
    option = random.choice(options)

    print("1. rock")
    print("2. paper")
    print("3. scissors")

    choice = input("enter your choice: ")

    if choice != "q":
        choice = int(choice)

        if options[choice - 1] == option:
            count += 1
            print()
            print("won!")
            print()

        else:
            print()
            print("lost")
            print(option)
            print()

    else:
        choice = "q"
