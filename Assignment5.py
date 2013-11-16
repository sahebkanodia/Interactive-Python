# implementation of card game - Memory

import simplegui
import random

l = range(0,8) + range(0,8)
random.shuffle(l)
exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]	
turns = 0

# helper function to initialize globals
def new_game():
    global state, exposed, l
    random.shuffle(l)
    state = 0
    turns = 0
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]	


     
# define event handlers
def mouseclick(pos):
    global exposed, state, turns, card1, card2
    i = pos[0]//50

    # add game state logic here
    if state == 0:
        if exposed[i] == False:
            exposed[i] = True
            card1 = i
        state = 1
    elif state == 1:
        if exposed[i] == False:
            exposed[i] = True            
            card2 = i
            turns += 1	
        state = 2

    elif state == 2:
        if l[card1] != l[card2]:
            exposed[card1] = False
            exposed[card2] = False
        if exposed[i] == False:
            exposed[i] = True
            card1 = i
        state = 1
    else:
        state = 1
        
    #Update label
    label.set_text("Turns = " + str(turns))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, turns
    card_pos = 10
    x = 0
    for num in l:
        if exposed[x] == True:
            canvas.draw_text(str(num), (card_pos, 70), 60, "White")
        else:
            canvas.draw_polygon([(card_pos-10, 0), (card_pos-10, 100), (card_pos+40, 100), (card_pos+40, 0)], 2, "Black", "Green")
        x += 1
        card_pos += 50

    #Check to see if all cards are paired
    paired = 0
    for i in exposed:
        if i:
            paired += 1
    if paired == 16:
        canvas.draw_text("You won! Total turns = " + str(turns)+ ". Please click Restart to play again.", (150,95), 18, "Red")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
# Developed by Saheb Kanodia
#http://www.codeskulptor.org/#user24_dJbfvUX9OQq4oYP_0.py
