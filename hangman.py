# lib imports
import random

# local imports
from words import word_list

tries = 0
# Define some Functions

# 1- a function to randomly get a word -- seed you app with data


def get_word():
    game_word = random.choice(word_list)
    return game_word.upper()


def play_game(game_word):
    word_completion = "_" * len(game_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    # tries = 6  # number of hangman body parts before a loss


def display_hangman(tries):
    stages = [  # 6: final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # 5: head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # 4: head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # 3: head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # 2: head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # 1: head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # 0: initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


# Invoke
print(get_word())
print(display_hangman(tries))

# if not main fxn disclaimer
