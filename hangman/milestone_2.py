import random

word_list = ["peach", "mango", "blackberry", "coconut", "grapefruit"]
word = random.choice(word_list)

guess = input("Guess a letter\n")

if guess == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")

    