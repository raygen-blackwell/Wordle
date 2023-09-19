# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

CORRECT_COLOR = "#66BB66"  # A shade of green
PRESENT_COLOR = "#CCBB66"  # A shade of brownish yellow
MISSING_COLOR = "#999999"  # A shade of gray


def wordle():

    gw = WordleGWindow()

    # Select a random secret word from the list
    secret_word = random.choice(FIVE_LETTER_WORDS)
    # Display secret word for testing purposes
    for i in range(len(secret_word)):
        gw.set_square_letter(0, i-1, secret_word[i-1].upper())

    def enter_action(s):
        guess = s[:N_COLS]
        # Check to see if the word is in the word list
        if guess.lower() in FIVE_LETTER_WORDS:
            gw.show_message("It's a valid word")

            # Check each letter in our string and see if the same letter is in secret word
            for i in range(len(secret_word)):
                for j in range(len(secret_word)):


                    #if the character is in the correct place, color that character green on the board and the keyboard
                    if (secret_word[i-1].lower() == guess[j-1].lower() and i==j):
                        gw.set_square_color(gw.get_current_row(),i-1,CORRECT_COLOR)
                        gw.set_key_color(secret_word[i-1].upper(),CORRECT_COLOR)
                    
                    #if the character is in the word, but not the correct place, color it yellow on the board
                    if gw.get_square_color(gw.get_current_row(),i-1) != CORRECT_COLOR:    
                        if (guess[i-1].lower() == secret_word[j-1].lower() and i!=j):
                            gw.set_square_color(gw.get_current_row(),i-1,PRESENT_COLOR)
                            
                        #if the character is not in the word, color it grey on both the board and the keyboard
                        if (guess[i-1].lower() not in secret_word):
                            gw.set_square_color(gw.get_current_row(),i-1,MISSING_COLOR)
                            gw.set_key_color(guess[i-1].upper(),MISSING_COLOR)
                        

                    


            # Move down to the next row
            rowNum = gw.get_current_row()
            if rowNum < N_ROWS - 1:
                gw.set_current_row(rowNum + 1)
            
        else:
            gw.show_message("Not in word list")


        if guess.lower() == secret_word.lower():
            gw.show_message("CONGRATULATIONS! YOU GUESSED THE WORD!")
        

    gw.add_enter_listener(enter_action)

# Startup code


if __name__ == "__main__":
    wordle()
