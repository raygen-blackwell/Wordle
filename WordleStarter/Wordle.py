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
    secret_word = 'chart'
    secret_word = random.choice(FIVE_LETTER_WORDS)
    for i in range (len(secret_word)):
        gw.set_square_letter(0,i-1,secret_word[i-1])


    def enter_action(s):
        
        row = s[:N_COLS]
        if row.lower() in FIVE_LETTER_WORDS:
            gw.show_message("First 5 row entered: " + row)
        else:
            gw.show_message("Not in word list")
    
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()
