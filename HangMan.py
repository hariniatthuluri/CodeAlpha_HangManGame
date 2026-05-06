import random

# -----------------------------
# Hangman Word Database
# -----------------------------
words = {
    "python": "Programming Language",
    "laptop": "Technology",
    "elephant": "Animal",
    "football": "Sport",
    "pizza": "Food"
}

# Hangman stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

def play_game():
    word, category = random.choice(list(words.items()))
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    display_word = ["_"] * len(word)

    print("\n🎮 Welcome to Hangman!")
    print(f"💡 Hint Category: {category}")

    while incorrect_guesses < max_attempts and "_" in display_word:

        print(hangman_stages[incorrect_guesses])
        print("\nWord:", " ".join(display_word))
        print("Guessed Letters:", ", ".join(guessed_letters))

        guess = input("\nEnter a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter only ONE alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in word:
            print("✅ Correct!")

            for index in range(len(word)):
                if word[index] == guess:
                    display_word[index] = guess

        else:
            incorrect_guesses += 1
            print("❌ Wrong guess!")

    # Final result
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print(hangman_stages[incorrect_guesses])
        print("\n💀 Game Over!")
        print("The word was:", word)

# -----------------------------
# Main Loop
# -----------------------------
while True:
    play_game()

    replay = input("\nDo you want to play again? (y/n): ").lower()

    if replay != "y":
        print("\n👋 Thanks for playing!")
        break