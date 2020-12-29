# OOP version of my ping pong game



# OBJECT 1 - SCREEN

# # Score
# score_a = 0
# score_b = 0

# Classes are templates to create objects

'''
The ping pong game has 4 objects:

The screen (done)
The two paddles
The ball
The score board

'''

import turtle

win = turtle.Screen()

win.title("Pong Game by Ivory")
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0)


class game_obj:
    def __init__(self, color, shape, speed, y):
        self.turtle = turtle.Turtle()
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.shape(shape)
        self.turtle.speed(speed)

# Paddles

# Paddle a
paddle_a = game_obj('black', 'square', 0)
paddle_a.turtle.goto(-350, 0)
paddle_a.turtle.shapesize(stretch_wid=5, stretch_len=1)

# Paddle b
paddle_b = game_obj('black', 'square', 0)
paddle_b.turtle.goto(350, 0)
paddle_b.turtle.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = game_obj('black', 'circle', 0)
ball.turtle.goto(0, 0)

# pen
pen = game_obj('black', None, 0)
pen.turtle.hideturtle()
pen.turtle.goto(0, 240)
pen.turtle.write("Player A:0  Player B:0", align="center", font=("Courier", 20, "normal"))


# Functions

    # Paddle_a_up
def paddle_a_up():
    y = paddle_a.turtle.ycor()
    y += 20
    paddle_a.turtle.sety(y)
    

# Calling the function on event
win.listen()
win.onkeypress(paddle_a_up(), 'w')
    

# Main game loop
while True:
    win.update()
        

        
    