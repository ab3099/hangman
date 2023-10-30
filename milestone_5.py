# Hangman class
import random

class Hangman():
  """
  A class representing a Hangman game.
  """
  def __init__(self, word_list, num_lives=5):
     """
    Initialize a new Hangman game.

    Parameters:
        - word_list (list): A list of words to choose from for the game.
        - num_lives (int): The number of lives the player has (default is 5).
     This method sets up the initial state of the Hangman game.

    Attributes:
        - self.word_list (list): The list of words available for the game.
        - self.num_lives (int): The number of lives the player has.
        - self.word (str): The word to guess, randomly chosen from word_list.
        - self.word_guessed (list): A list representing the word to guess, initially filled with underscores.
        - self.num_letter (set): A set containing the unique letters in the word.
        - self.num_letters (int): The count of unique letters in the word.
        - self.list_of_guesses (list): A list to store the player's guesses.

        The self.word_guessed list is initially filled with underscores to represent hidden letters.
        The self.num_letter set is used to track unique letters in the word, and
        self.num_letters stores the count of these unique letters.
        The self.list_of_guesses will store the player's guessed letters.
        """
 
     self.word_list= word_list
     self.num_lives= int(num_lives)
     self.word= random.choice(self.word_list)
     self.word_guessed= ["_" for _ in self.word]
     self.num_letters = len(set(self.word))  # Count of unique letters in the word
     self.list_of_guesses = []
  
  def check_guess(self, guess):
    """
     Check if the guessed letter is in the word.

    Parameters:
      - guess (str): The letter guessed by the player.

    If the guessed letter is in the word, it updates the word_guessed and decreases the number
        of unique letters remaining. If the guess is incorrect, it decreases the number of lives.
    """
    guess= guess.lower()
    if guess in self.word:
        print("Good guess! ' " + guess + " ' is in the word.")
        for i in range(len(self.word)):
            if self.word[i] == guess:
              self.word_guessed[i] = guess
              self.num_letters -= 1
    else: 
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    return 
  def ask_for_input(self):
    """
    Prompt the player for a single letter guess and handle the input.

    It checks if the input is a single alphabetical character and whether it has already been
    guessed. If the input is valid, it calls the check_guess method.
    """
    self.guess= input("Enter a single letter: ")
    if len(self.guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
    elif   self.guess in self.list_of_guesses: 
            print("You already tried that letter!")
    else:
            self.check_guess(self.guess)
            self.list_of_guesses.append(self.guess)
    return 
def play_game(word_list):
 num_lives = 5 
 i = 0
 game = Hangman(word_list, num_lives)
 lives = game.num_lives
 while True:
    print("hell")
    if lives == 0: 
            print("You lost!")
            break
    elif game.num_letters > 0:
        game.ask_for_input()
        lives = game.num_lives
        print(lives)
    else:
            print("Congratulations. You won the game!")
            break

play_game(["cat","dog","rat","fox"])



