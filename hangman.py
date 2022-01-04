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
    word_completion = "_" * len(game_word)  # clever
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries_remaining = 6  # number of hangman body parts before a loss

    # 2: print start game instructions
    print("-------------------")
    print("Let's Play Hangman!")
    print(game_word)  # debug - the word at hand
    print(render_hangman(tries_remaining))  # the hangman state
    print(f'{word_completion}\n')  # the word as _ _ _ _ _

    # 2.1: game logic
    while not guessed and tries_remaining > 0:
        guess = input("Please guess a letter or word: ").upper()
        # case: guessing a letter
        if len(guess) == 1 and guess.isalpha():
            # a- on already guessed letter
            if guess in guessed_letters:
                print(f'You already guessed the letter "{guess}"')
            # b- on incorrect letter guess
            elif guess not in game_word:
                print(f'the letter "{guess}" is not in the word')
                # decrement tries
                tries_remaining -= 1
                # add letter to guessed letters list
                guessed_letters.append(guess)
            # c- on correct letter guess # TODO: create a fxn for this to improve readability
            else:
                print(f'Good guess: {guess} is in the word')
                guessed_letters.append(guess)
                # update word completion
                # a- change from string to list so we can index into it
                word_as_list = list(word_completion)
                # b- check word for all instances of letter via a list comprehension
                indices = [i for i, letter in enumerate(
                    game_word) if letter == guess]
                for index in indices:
                    # place the guessed letter where it goes in the word
                    word_as_list[index] = guess
                # convert back to string - str() better?
                word_completion = "".join(word_as_list)
                # Also need to check if this guess completes the word (and ends the game)
                # how - check for _ in word completion (if none, all letters)
                # ? couldn't you just check if word_completion == game_word ?
                if "_" not in word_completion:
                    guessed = True  # this ends the game
        # guessing a word
        elif len(guess) == len(game_word) and guess.isalpha():
            # a- on already guessed word
            if guess in guessed_words:
                print(f'You already guessed the word "{guess}"')
            # b- on incorrect guessed word
            elif guess != game_word:
                print(f'Incorrect word guess. Please try again')
                # decrement the tries
                tries_remaining -= 1
                # append this word to the guessed_words
                guessed_words.append(guess)
            # c- on correct guessed word
            else:
                guessed = True
                word_completion = game_word
        # error case - better coding would put this first
        else:
            print("Sorry, not a valid guess, Please try again.")

        # 2.2: render updated state of the game
        print(f'debug: tries remaining is now {tries_remaining}')
        print(render_hangman(tries_remaining))  # the hangman state
        print(f'{word_completion}\n')

    if guessed:  # Truthy check for winning the game
        print("Congrats, you guessed the word. You Win")
    else:  # Ran out of tries - it will exit the while loop after 6 tries
        print(
            f'Sorry, you ran out of tries. The word was {game_word}. Maybe next time')


def render_hangman(tries):
    game_states = [  # 0 tries: final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # 1 try left: head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # 2 tries left: head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # 3 tries left: head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # 4 tries left: head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # 5 tries left: head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # 6 tries left: initial empty state
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
    return game_states[tries]  # string ascii art


# Invoke the Game
def main():
    play_game(get_word())
    while input("Play Again? (Y/N) ").upper() == 'Y':
        play_game(get_word())


# add if not main fxn disclaimer
# (to prevent code from running on import and allow it to run on the cli)
if __name__ == "__main__":
    main()
