"""Snowman Meltdown: guess the secret word letter by letter."""
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = 3


def get_random_word():
    """Select and return a random word from the list."""
    return random.choice(WORDS)


def play_game():
    """Play one round: the player guesses letters until the word is found
    or the maximum number of mistakes is reached."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")

    while mistakes < MAX_MISTAKES:
        guess = input("Guess a letter: ").lower()
        guessed_letters.append(guess)
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            mistakes += 1
            print(f"Sorry, '{guess}' is not in the word.")
        print(" ".join(letter if letter in guessed_letters else "_"
                       for letter in secret_word))
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations, you saved the snowman!")
            return
    print(f"Game Over! The word was: {secret_word}")


if __name__ == "__main__":
    play_game()
