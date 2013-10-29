# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random


# initialize global variables used in your code

x=0
low =0
high = 100
n =7
# helper function to start and restart the game
def new_game():
    global x, low, high, n
    x = random.randint(low, high)
    f.start()

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global low, high, n
    low = 0
    high = 100
    n = 7
    print "New Game. Range is 0 to 100"
    print "Allowed Attempts = 7\n"
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global low, high, n
    low = 0
    high = 1000
    n = 10
    print "New Game. Range is 0 to 1000" 
    print "Allowed Attempts = 10\n"
    new_game()   
    
def input_guess(guess):
    # main game logic goes here	
    global x, n, low, high
    num = int(guess)
    if n>0:
        print "User guess is = ",num
        n=n-1
        if x==num:
            print "Correct!\n"
            if high == 1000:
                range1000()
            else:
                range100()
        elif x>num:
            print "Higher!"
            print "Remaining attempts = ", n
            print "\n"
        elif x<num:
            print "Lower!"
            print "Remaining attempts = ", n
            print "\n"
    else:
        if high == 1000:
            range1000()
        else:
            range100()

        
        
    
# create frame

f=simplegui.create_frame("Game", 250, 250)


# register event handlers for control elements

f.add_button("Range is [0 to 100]", range100, 200)
f.add_button("Range is [0 to 1000]", range1000, 200)
f.add_input("Enter you guess", input_guess , 150)

# call new_game and start frame

new_game()
f.start()
range100()

# always remember to check your completed program against the grading rubric
# http://www.codeskulptor.org/#user21_d5oXwhF05E_0.py
