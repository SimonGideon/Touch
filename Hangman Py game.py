import random
name = input("Enter your Name:")
print("All the best", name)
words = ["website", "hangman", "rainbow", "computer", "science", "programming", "python", "mathematics", "player"]
word = random.choice(words)
print("\nGuess the characters")
guesses = ""
turns = 10 # Number of turns
while turns >0:
    failed = 0 # Cont the number of times a user fails.
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end="")
            failed += 1
    if failed == 0:
        print("\n\nYou Win")
        print("\nthe word is", word)
        break
    guess = input("\nguess te character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        # If the character does not match print wrong.
        print("\nwrong")
        print("\nYou have", +turns, "more guesses")
        if turns == 0:
            print("\nYou have lost.")
