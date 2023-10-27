import random
fruit_list = ["apple", "banana","rasberry", "fig", "watermelon"]
print(fruit_list) 

#random choice
word = random.choice(fruit_list)
print(word)
guess = input("Enter a single letter:")


def check_guess(guess):
    
    guess = guess.lower()
    if guess in word: 
     print("Good guess! ' " + guess + " ' is in the word.")
    else: 
     print("Sorry, ' " + guess + " ' is not in the word. Try again.")

def ask_for_input(guess):
 while True:
    
    
    if len(guess) == 1 and guess.isalpha():
      print("You've entered a valid character") 
      break 
    else: 
      print("Invalid letter. Please, enter a single alphabetical character.")

check_guess(guess)


test_1= ask_for_input(guess)

