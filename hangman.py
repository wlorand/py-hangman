# lib imports
import random

# local imports
from words import word_list

# Define some Functions

# 1- a function to randomly get a word -- seed you app with data


def get_word():
    game_word = random.choice(word_list)
    return game_word.upper()


def play_game(game_word):

    # 1- define your vars
    word_completion = "_ " * len(game_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6  # number of hangman body parts before a loss

    # 2- print start game instructions
    print("Let's Play Hangman!")
    print(game_word)  # debug - the word at hand
    print(display_hangman(tries))  # the hangman
    print(word_completion)  # the word


def display_hangman(tries):
    game_states = [  # 6: final state: head, torso, both arms, and both legs
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
    return game_states[tries]


# Invoke
word = get_word()
# print(display_hangman(tries))
play_game(word)

# if not main fxn disclaimer
