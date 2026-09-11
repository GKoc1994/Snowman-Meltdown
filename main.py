import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

class Snowman:
  def __init__(self):
    self.mistakes = 0 
    self.correct_chars = []
    self.secret_word= get_random_word()
    self.user_input = " "
    self.max_mistakes = 6
    self.game_over = False

  def greet_user(self):
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    print("_ " * len(self.secret_word))

  def get_letter(self):
    while True:
      self.user_input = input( "Guess a letter: ").lower()
      input_not_alpha = self.user_input.isalpha()
      input_formated = len(self.user_input)
      input_in_correct_list = False
      input_in_mistake_list = code
      if not (len(self.user_input) == 1 and self.user_input.isalpha()):
        break
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
  
  def compare_letters(self):
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

  def evaluate_results(self):
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

  def inform_user(self):
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

def play_game():
    game = Snowman()
    game.greet_user()
    game.get_letter()
    game.compare_letters()
    game.evaluate_results()
    game.inform_user()
    # TODO: Build your game loop here.
    # For now, simply prompt the user once:
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)
    
if __name__ == "__main__":
    play_game()
