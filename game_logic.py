"""Game logic of Snowman Meltdown: word selection, guessing and game loop."""
import random

from ascii_art import STAGES

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


def ask_play_again():
    """Ask the user if they want to play another round."""
    while True:
        answer = input("Do you want to play again? (y/n): ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please enter 'y' or 'n'.")
