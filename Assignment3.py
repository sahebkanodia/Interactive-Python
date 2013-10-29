# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 100
x = 0
y = 0
timer_state = False
sp = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    d = t%10
    c = ((t%100)- (d))/10
    a = int(t/600)
    b = ((t%600) - (c*10) - d)/100
    return (str(a)+':'+ str(b)+str(c)+'.'+ str(d))


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    global sp
    timer.start()
    sp = sp + 1

def stop_button():
    global x, y, timer_state
    timer.stop()
    y = y + 1
# Checking if timer is running to update score
    timer_state = timer.is_running()
    if timer_state == False:
        if (time%10) ==0:
            x =x+1
    
def reset_button():
    global time,x,y
    timer.stop()
    time = 0
    x = y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time = time + 1

# define draw handler
def draw(canvas):
    global time,x,y
    s = format(time)
    canvas.draw_text(str(s), [130,100], 20, 'Cyan')
    canvas.draw_text(str(x)+' / '+str(y), [260,25], 12, 'Cyan' )
    
# create frame
frame= simplegui.create_frame("Stopwatch", 300, 200)
start= frame.add_button("Start", start_button)
stop= frame.add_button("Stop", stop_button)
reset = frame.add_button("Reset", reset_button)

#create timer
timer = simplegui.create_timer(time, timer_handler)

# register event handlers
frame.set_draw_handler(draw)


# start frame
frame.start()
time = 0
timer.stop()

# Please remember to review the grading rubric
# http://www.codeskulptor.org/#user22_B2YN6Jg6R1d4JtP_0.py
