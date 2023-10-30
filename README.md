# Hangman
# Table of content
1. [Introduction](#introduction)
2. [How it works](#How-it-works-?)
3. [Hangaman Milestones](#section-1)
    - [Defining Hangman functions](#Defining-Hangaman-functions)
    - [Hangman game class](#Hangan-game-class)

## Introduction 
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
## How it works?
The computer randomly choses a word from a list of words and the user tries to guess it.

## Milestones
### Defining Hangman functions 
These functions are part of the Hangman game, allowing players to make guesses and checking if their guesses match the randomly selected word.

**Step 1:**
- Create a list containing the names of your 5 favorite fruits
- Select a random word from the list using the random.choice function

**Step 2:**

### `check_guess(guess)` 


_The `check_guess` function takes a guessed letter as an argument and checks if the letter is in the word._

**Function's set up:**

**1.** Define a function called `check_guess` that accepts a single parameter, `guess`.

**2.** Convert the `guess` into lowercase to ensure case-insensitive matching.

**3.** Determine if the `guess` is in the randomly selected word. If it is, display a success message. If not, display an error message.

**Step 3:**
### `ask_for_input()`

_The `ask_for_input` function prompts the player to input a single letter and checks its validity._

**Function's set up:**

**1.** Define a function called `ask_for_input`.

**2.** Move the code that checks if the input is a valid guess into this function.

**3.** Use a `while` loop to repeatedly request input until a valid, single alphabetical character is entered.

**4.** Call the `check_guess` function from within the `ask_for_input` function to check if the guess is in the word.

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

**Paramater**: guess - letter guessed by the player.

If the guessed letter is in the word: 

- it updates the list of letters representing the word to guesssed 

- decreases the number of unique letters remaining. If the guess is incorrect, it decreases the number of lives.

`ask_for_input(self)`

Prompts the player to input a single letter guess.

- ensures the input is a single alphabetical character and hasn't been guessed before, 
- it calls the check_guess method to verify if the guess is in the word.




## Usage

To play the Hangman game based on this code:

1. Run the Python script (`hangman.py`) on your computer.

2. The computer will randomly select a word from the provided list of fruit names.

3. Enter a single letter when prompted.

4. The game will check the validity of the input, and if it's a valid character, it will check if the letter is in the word. You will receive feedback accordingly.

5. Continue guessing letters until you guess the word or run out of attempts.


**Prerequisites:**

- Python 3.7+ installed on your computer.

**Installation:**

1. Clone this repository to your local machine:



