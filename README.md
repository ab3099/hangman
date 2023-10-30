# Hangman
# Table of content
1. [Introduction](#introduction)
2. [How it works](#How-it-works-?)
3. [Defining Hangman functions](#Defining-Hangaman-functions)
4. [Hangman game class](#Hangan-game-class)
5. [Play the game](#Play-the-game)
6. [Prerequisites](#Prerequisites)

## Introduction 
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
## How it works?
The computer randomly choses a word from a list of words and the user tries to guess it.


### Defining Hangman functions 
These functions are part of the Hangman game, allowing players to make guesses and checking if their guesses match the randomly selected word.

**Step 1:**
- Create a list containing the names of your 5 favorite fruits
- Select a random word from the list using the random.choice function

**Step 2:**

### `check_guess(guess)` 


_The `check_guess` function takes a guessed letter as an argument and checks if the letter is in the word._

**Function's set up:**
guess (str): The letter guessed by the player.

**Functionality:**

1. It converts the guess to lowercase to ensure case-insensitive matching.

2. If the guessed letter is in the word, it updates the word_guessed to reveal the correctly guessed letters and decreases the number of unique letters remaining (num_letters).

3. If the guess is incorrect, it decreases the number of lives (num_lives) and provides feedback to the player.


### `ask_for_input()`

_The `ask_for_input` function prompts the player to input a single letter and checks its validity._

**Functionality:**

1. It prompts the player to input a single letter guess.

2. It checks if the input is a single letter and whether it has already been guessed.

3. If the input is valid, it calls the check_guess method to validate the guess and update the game state.

## The hangman class
_The Hangman game class is the core component responsible for managing the game, player interaction, and word selection._

**Class Initialization**

To create an instance of the Hangman game, you need to initialize it with a list of words and an optional number of lives for the player:

```python
my_instance = Hangman(["cake", "tea", "coffee"], 5)
```
**Attributes**

- self.word_list (list): The list of words available for the game.

- self.num_lives (int): The number of lives the player has.
- self.word (str): The word to guess, randomly chosen from  word_list.
- self.word_guessed (list): A list of letters representing the word to guess, initially filled with underscores to hide the letters.
- self.num_letter (set): A set containing the unique letters in the word.
- self.num_letters (int): The count of unique letters in the word.
- self.list_of_guesses (list): A list to store the player's guessed letters.

**Methods**

`check_guess(self, guess)`

`ask_for_input(self)`


## Play the game

Define the Play_game function. 
```python
def play_game(word_list):
```
**Paramater**: world_list - A list of words from which the Hangman game selects a word for the player to guess.

To play, follow these steps:

**1.**  Initialize `num_lives` to 5.

**2.** Create a Hangman game instance (`game`) with  `word_list` and `num_lives`.

**3**. Start a loop:

    - If `num_lives` reach 0, you lose, and the game ends.
    - If there are still letters to guess, the game prompts you for input.


## Prerequisites


1. Python 3.11.5 installed on your computer

2. clone the git repository: https://github.com/ab3099/hangman.git

3. Run the Python script (`milestone_5.py`) on your local machine





