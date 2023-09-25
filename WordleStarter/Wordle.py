# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import tkinter

from WordleDictionary import FIVE_LETTER_WORDS_ENGLISH
from WordleDictionary import FIVE_LETTER_WORDS_DUTCH
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS






def wordle():

    CORRECT_COLOR = "#66BB66"  # A shade of green
    PRESENT_COLOR = "#CCBB66"  # A shade of brownish yellow
    MISSING_COLOR = "#999999"  # A shade of gray

    myList = FIVE_LETTER_WORDS_ENGLISH

    root = tkinter.Tk()
    root.title("Color Scheme and Language Settings")

    def button1_click():
        nonlocal myList
        label.config(text="Settings Changed! Language is now Dutch :)")
        myList = FIVE_LETTER_WORDS_DUTCH
        show_word()
        
    def button2_click():
        nonlocal CORRECT_COLOR
        nonlocal PRESENT_COLOR
        nonlocal MISSING_COLOR
        CORRECT_COLOR = "#1974d2" # A shade of blue
        PRESENT_COLOR = "#fff68f" # A shade of nicer yellow
        MISSING_COLOR = "#cc3333" # A shade of red
        label.config(text="Settings Changed! Colors are now Blue/Yellow/Red")
        
    label = tkinter.Label(text="")
    label.pack()
    
    button = tkinter.Button(text = "CHANGE LANGUAGE TO DUTCH", command=button1_click)
    button.pack()
    button2 = tkinter.Button(text = "CHANGE COLOR SCHEME", command=button2_click)
    button2.pack()
    

    # if button1_clicked == True:
    #     myList = FIVE_LETTER_WORDS_DUTCH
    # else:
    #     myList = FIVE_LETTER_WORDS_ENGLISH

    
    def show_word():
    # Select a random secret word from the list
        global secret_word
        secret_word = random.choice(myList)
        # Display secret word for testing purposes
        for i in range(len(secret_word)):
            gw.set_square_letter(0, i-1, secret_word[i-1].upper())
    
    guess_count = 0

    def enter_action(s):
            nonlocal guess_count
            if guess_count < 6:
                guess = s[:N_COLS]
                # Check to see if the word is in the word list
                if guess.lower() in myList:
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
                                    if gw.get_key_color(guess[i-1].upper()) != CORRECT_COLOR:
                                        gw.set_key_color(guess[i-1].upper(),PRESENT_COLOR)
                                    #TODO figure out how to show the correct number of yellow squares
                                    
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
                    guess_count = 10

                guess_count +=1
                if guess_count == 6 and (guess.lower() != secret_word.lower()):
                    gw.show_message("You lost! Start the program over to try again!")

            else:
                return
                
    gw = WordleGWindow() 
    gw.add_enter_listener(enter_action)
    show_word()

# Startup code


if __name__ == "__main__":
    wordle()
