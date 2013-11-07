# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
ball_pos = [WIDTH/2, HEIGHT/2]
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = False
x = random.randrange(2,4)
y = random.randrange(2,4)
ball_vel = [x, -y]
paddle1_pos = [HEIGHT/2 - HALF_PAD_HEIGHT, HEIGHT/2 + HALF_PAD_HEIGHT]
paddle2_pos = [HEIGHT/2 - HALF_PAD_HEIGHT, HEIGHT/2 + HALF_PAD_HEIGHT]
score1 = 0
score2 = 0
paddle1_vel = 0
paddle2_vel = 0
direction = False

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, score1, score2 # these are vectors stored as lists
    global x,y, LEFT,RIGHT
    if direction == RIGHT or direction == LEFT:
        ball_vel[0] = -(ball_vel[0])

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global direction
    score1 = 0
    score2 = 0
    spawn_ball(direction)

    if direction == RIGHT:
        ball_vel = [x, -y]
    elif direction == LEFT:
        ball_vel = [-x, -y]

def draw(c):
    global HEIGHT, score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, BALL_RADIUS, paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0] 
    ball_pos[1] = ball_pos[1] + ball_vel[1] 

    #collide the ball and reflect off of the vertical walls
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT- BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    
    #Checking ball collision with paddle
    if ball_pos[0] <= BALL_RADIUS: 
        if ball_pos[1] >= paddle1_pos[0] and ball_pos[1] <= paddle1_pos[1]:
            spawn_ball(LEFT)
        else:
            score2 += 1
            ball_pos = [WIDTH/2, HEIGHT/2]
            spawn_ball(LEFT)
    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        if ((ball_pos[1]) >= paddle2_pos[0]) and ((ball_pos[1]) <= paddle2_pos[1]):
            spawn_ball(RIGHT)
        else:
            score1 += 1
            ball_pos = [WIDTH/2, HEIGHT/2]
            spawn_ball(RIGHT)

    # draw ball    
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Grey", "Grey")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] = paddle1_pos[1] + paddle1_vel
    paddle1_pos[0] = paddle1_pos[0] + paddle1_vel
    paddle2_pos[1] = paddle2_pos[1] + paddle2_vel
    paddle2_pos[0] = paddle2_pos[0] + paddle2_vel
    if paddle1_pos[0] <= 0 or paddle1_pos[1]>= HEIGHT:
        paddle1_vel =0
    if paddle2_pos[0] <= 0 or paddle2_pos[1]>= HEIGHT:
        paddle2_vel =0    
    
    # draw paddles
    c.draw_line([0, paddle1_pos[0]], [0, paddle1_pos[1]], (PAD_WIDTH+5), "Dark Grey" )
    c.draw_line([WIDTH - PAD_WIDTH + 6, paddle2_pos[0]], [WIDTH-PAD_WIDTH+6, paddle2_pos[1]], (PAD_WIDTH), "Dark Grey" )

    # draw scores
    c.draw_text(str(score1), (200, 75), 36, 'White')
    c.draw_text(str(score2), (375, 75), 36, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel, LEFT, RIGHT, direction
    if key == simplegui.KEY_MAP["right"]:
       RIGHT = True        
    elif key == simplegui.KEY_MAP["left"]:
       LEFT = True
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 4
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 4
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 4
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 4


def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0

def restart():
    global score1, score2, WIDTH, HEIGHT, ball_pos, acc, paddle1_pos, paddle2_pos
    score1 = 0
    score2 = 0
    ball_pos = [WIDTH/2, HEIGHT/2]
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', restart, 100)

# start frame
new_game()
frame.start()
new_game()

#Developed by Saheb Kanodia
