random_number = 76
guessnum = None

while guessnum != random_number:
    guessnum = int(input("Enter a number (0 to quit): "))

    if guessnum == 0:
        print("You Lose")
        break
    elif guessnum > random_number:
        print("Guessed number is larger")
    elif guessnum < random_number:
        print("Guessed number is smaller")
    else:
        print("You Won!")
