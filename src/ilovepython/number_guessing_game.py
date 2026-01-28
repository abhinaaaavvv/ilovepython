import random

guess = int(input("enter a number from 1 to 100: "))
random_number = random.randint(1, 100)
count = 0

while guess != random_number:
    if guess > random_number:
        print("your guess is greater than actual number")
        print()
        guess = int(input("enter a number from 1 to 100: "))
        count += 1

    elif guess < random_number:
        print("your guess is less than actual number")
        print()
        guess = int(input("enter a number from 1 to 100: "))
        count += 1

if guess == random_number:
    print("ur guess is equal to actual number")
    print()
    print("you guessed the number in", count, "attempts")
