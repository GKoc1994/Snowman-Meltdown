"""Snowman Meltdown: guess the secret word before the snowman melts."""
import random

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
     ___
    /___\\
    (o o)
    ( : )
    ( : )
    """,
    # Stage 1: Bottom part starts melting
    """
     ___
    /___\\
    (o o)
    ( : )
    """,
    # Stage 2: Only the head remains
    """
     ___
    /___\\
    (o o)
    """,
    # Stage 3: Snowman completely melted
    """
     ___
    /___\\
    """
]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Select and return a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Print the snowman for the current number of mistakes and the word,
    with the letters that were not guessed yet shown as underscores."""
    print(STAGES[mistakes])
    display_word = " ".join(letter if letter in guessed_letters else "_"
                            for letter in secret_word)
    print("Word:", display_word)
    print()


def get_guess(guessed_letters):
    """Ask the user for a letter until a single new letter is entered."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
        else:
            return guess


def is_word_guessed(secret_word, guessed_letters):
    """Return True if every letter of the secret word was guessed."""
    return all(letter in guessed_letters for letter in secret_word)


def play_game():
    """Play one round of Snowman Meltdown until the player wins or loses."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < MAX_MISTAKES:
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            mistakes += 1
            print(f"Sorry, '{guess}' is not in the word.")

        display_game_state(mistakes, secret_word, guessed_letters)

        if is_word_guessed(secret_word, guessed_letters):
            print("Congratulations, you saved the snowman!")
            return True

    print(f"Game Over! The snowman melted. The word was: {secret_word}")
    return False



if __name__ == "__main__":
    play_game()
