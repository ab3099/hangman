# Hangman
# Table of content
1. [Introduction](#introduction)
2. [How it works](#How-it-works-?)
2. [Installation Instructions](#section-1)
    - [Subsection 1.1](#subsection-1.1)
    - [Subsection 1.2](#subsection-1.2)

## Introduction 
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
## How it works?
The computer thinks of a word and the user tries to guess it.

## Defining variables

Step 1:
Create a list containing the names of your 5 favorite fruits.

Step 2:
Choose a random word from the list using random.choice function.

## Functions

### `check_guess(guess)`

The `check_guess` function takes a guessed letter as an argument and checks if the letter is in the word.

**Step 1:** Define a function called `check_guess` that accepts a single parameter, `guess`.

**Step 2:** Convert the `guess` into lowercase to ensure case-insensitive matching.

**Step 3:** Determine if the `guess` is in the randomly selected word. If it is, display a success message. If not, display an error message.

### `ask_for_input()`

The `ask_for_input` function prompts the player to input a single letter and checks its validity.

**Step 1:** Define a function called `ask_for_input`.

**Step 2:** Move the code that checks if the input is a valid guess into this function.

**Step 3:** Use a `while` loop to repeatedly request input until a valid, single alphabetical character is entered.

**Step 4:** Call the `check_guess` function from within the `ask_for_input` function to check if the guess is in the word.

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

