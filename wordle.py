import random
from colorama import Fore, Style

WORD_LIST = "https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93.js

def get_feedback(guess, secret):
    feedback = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            feedback.append(Fore.GREEN + guess[i] + Style.RESET_ALL)  # Correct position
        elif guess[i] in secret:
            feedback.append(Fore.YELLOW + guess[i] + Style.RESET_ALL)  # Correct letter
        else:
            feedback.append(guess[i])  # Incorrect letter
    return ''.join(feedback)

def wordle_game():
    secret_word = random.choice(words)
    attempts = 6
    print("Welcome to Wordle! You have 6 attempts to guess the 5-letter word.")
    
    while attempts > 0:
        guess = input("Enter your guess (or type 'exit' to quit): ").lower()
        if guess == "exit":
            print("Thanks for playing!")
            break
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        
        if guess == secret_word:
            print(f"Congratulations! You've guessed the word '{secret_word}' correctly!")
            bre
        