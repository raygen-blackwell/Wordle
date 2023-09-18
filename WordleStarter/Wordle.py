# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

CORRECT_COLOR = "#66BB66" # A shade of green
PRESENT_COLOR = "#CCBB66" # A shade of brownish yellow
MISSING_COLOR = "#999999" # A shade of gray

def wordle():
    # Select a random secret word from the list
    # secret_word = random.choice(FIVE_LETTER_WORDS)
    gw = WordleGWindow()
    
    secret_word = random.choice(FIVE_LETTER_WORDS)
    for i in range (len(secret_word)):
        gw.set_square_letter(0,i-1,secret_word[i-1].upper())

    
    def enter_action(s):
        guess = s[:N_COLS]
        if guess.lower() in FIVE_LETTER_WORDS:
            gw.show_message("It's a valid word")

            # check each letter in our string and see if the same letter is in secret word
            for i in range(len(secret_word)):
                for j in range(len(secret_word)):

                    #if the character is in the correct place, color that square green
                    if (secret_word[i-1].lower() == guess[j-1].lower() and i==j):
                        gw.set_square_color(gw.get_current_row(),i-1,CORRECT_COLOR)
                    
                    #if the character is in the word, but not the correct place, color it yellow
                    if gw.get_square_color(gw.get_current_row(),i-1) != CORRECT_COLOR:    
                        if (guess[i-1].lower() == secret_word[j-1].lower() and i!=j):
                            gw.set_square_color(gw.get_current_row(),i-1,PRESENT_COLOR)


            rowNum = gw.get_current_row()
            if rowNum < N_ROWS -1:
                gw.set_current_row(rowNum + 1)
        else:
            gw.show_message("Not in word list")

        if guess.lower() == secret_word.lower():
            gw.show_message("CONGRATULATIONS! YOU GUESSED THE WORD!")
        
        

        # gw.add_enter_listener(enter_action)
    
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()
