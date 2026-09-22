import random

easy_words = ["money", "apple", "house", "ant"]
normal_words = ["football", "keyboard", "computer", "level"]
hard_words = ["cricket", "mango", "flowers", "speaker"]

print("Welcome to the Word Guessing Game")

while True:
    level = input("Select Level (easy, normal, hard): ").lower().strip()

    if level == "easy":
        word = random.choice(easy_words)
        break
    elif level == "normal":
        word = random.choice(normal_words)
        break
    elif level == "hard":
        word = random.choice(hard_words)
        break
    else:
        print("Please select a given level.")

attempts = 0
print("Guess the word!")

while True:
    guess = input("Enter your guess: ").lower().strip()
    attempts += 1

    if guess == word:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break

    hint = ""

    for i in range(len(word)):
        if i < len(guess) and guess[i] == word[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint:", hint)

print("Game Over")