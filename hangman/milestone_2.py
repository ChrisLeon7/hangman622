import random

word_list = ["peach", "mango", "blackberry", "coconut", "grapefruit"]
word = random.choice(word_list)
letter = True








def check_guess(guess):
    guess = guess.lower
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")   

def ask_for_input():
    if len(guess) == 1:
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
    while True:
        guess = input("Guess a letter\n").lower
        if guess.isalpha() == True:
            False
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

