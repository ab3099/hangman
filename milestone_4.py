# Hangman class
import random

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word_list= word_list
        self.num_lives= int(num_lives)
        self.word= random.choice(self.word_list)
        self.word_guessed= ["_" for _ in self.word]
        self.num_letter= set(self.word)
        self.num_letters = len(set(self.word))  # Count of unique letters in the word
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess= guess.lower()
        if guess in self.word:
            print(self.word)
            print("Good guess! ' " + guess + " ' is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                   self.word_guessed[i] = guess
            self.num_letters -= 1
        else: 
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    

    def ask_for_input(self):
     while True: 
        self.guess= input("Enter a single letter: ")
        if len(self.guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif   self.guess in self.list_of_guesses: 
            print("You already tried that letter!")
        else:
            self.check_guess(self.guess)
        self.list_of_guesses.append(self.guess)
        



my_instance= Hangman(["cake", "tea","pate"], 5 )
my_instance.ask_for_input()


