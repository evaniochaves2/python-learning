
for number in range(1, 51):
    guess = int(input(f"Guess a number between 1 and 50 (Attempt {number}): "))
    if guess == 17:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again.")
