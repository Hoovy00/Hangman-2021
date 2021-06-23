#!/usr/bin/env pythons
import random
from words import word_list

def get_random_word():
    '''get_random_word selects a random word from 'word_list', and returns it in uppercase'''
    word = random.choice(word_list)
    return word.upper()

def play_round_of_hangman(word):
    '''play_round_of_hangman is what runs the game itself'''
    currently_revealed = "_" * len(word)
    has_won = False
    guessed_letters = []
    guessed_words = []
    num_attempts_left = 6
    print("Let's play Hangman!")
    print(display_hangman(num_attempts_left))
    print(currently_revealed)
    print("\n")
    while (not has_won) and (num_attempts_left > 0):
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.") 
                num_attempts_left = num_attempts_left - 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(currently_revealed)
                for index, letter in enumerate(word):
                    if letter == guess:
                        word_as_list[index] = guess
                currently_revealed = "".join(word_as_list)
                if "_" not in currently_revealed:
                        has_won = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already num_attempts_left the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                num_attempts_left -=1
                guessed_words.append(guess)
            else: 
                has_won = True
                currently_revealed = word
        else:
            print("Not a valid guess.")
        print(display_hangman(num_attempts_left))
        print(currently_revealed)
        print("\n")
    if num_attempts_left:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
        
def display_hangman(num_attempts_left):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
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
    return stages[num_attempts_left]


def main():
    word = get_random_word()
    play_round_of_hangman(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_random_word()
        play_round_of_hangman(word)

if __name__ == "__main__":
    main()
