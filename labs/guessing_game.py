import random

start = 1
end = 1000
guess_count = 0
hidden_number = random.randint(start, end)

while True:
    user = input(f"Enter your guess from {start} to {end}: ")
    # check if user guess is a number
    if not user.isnumeric():
        continue
    user = int(user)
    # check if user guess is in between the range
    if start > user or user > end:
        continue
    # check guess count
    if guess_count > 10:
        print("You ran out of guesses!")
        break

    if user < hidden_number:
        start = user + 1
        guess_count += 1
    elif user > hidden_number:
        end = user - 1
        guess_count += 1
    else:
        print(f"You got it! The hidden number is {hidden_number}")
        print(f"It took you {guess_count} guess(es).")
