"""Start the Snowman Meltdown game."""
from game_logic import ask_play_again, play_game


def main():
    """Play rounds of Snowman Meltdown until the user wants to stop."""
    while True:
        play_game()
        if not ask_play_again():
            print("Thanks for playing Snowman Meltdown!")
            break


if __name__ == "__main__":
    main()
