from turtle import Turtle, Screen
from scoreboard import Score
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(height=500, width=1000)
screen.bgcolor("black")
screen.title("Ball Pong")

# Registering a rectangular shape
RECTANGLE = ((-10, 30), (10, 30), (10, -30), (-10, -30))
screen.register_shape('rectangle', RECTANGLE)

# Stopped screen updates
screen.tracer(0)
# Setting the delimitation of the screen
delim = Turtle()
delim.penup()
delim.hideturtle()
delim.pencolor("white")
delim.setposition(x=0, y=-250)
delim.setheading(90)
while delim.ycor() < 250:
    delim.pendown()
    delim.forward(20)
    delim.penup()
    delim.forward(20)

# Setting up the scores
p1_score = Score()
p1_score.setposition(x=-30, y=200)
p1_score.refresh()

p2_score = Score()
p2_score.setposition(x=30, y=200)
p2_score.refresh()

# Creating the paddles. P1 paddle is the one on the left, while p2 is on the right
p1_paddle = Paddle()
p1_paddle.setposition(x=-480, y=0)
p2_paddle = Paddle()
p2_paddle.setposition(x=470, y=0)

screen.update()
# Default screen updates
screen.tracer(1)

# Moving the paddles
def p1_paddle_up():
    p1_paddle.forward(30)

def p1_paddle_down():
    p1_paddle.backward(30)

def p2_paddle_up():
    p2_paddle.forward(30)

def p2_paddle_down():
    p2_paddle.backward(30)

screen.listen()
screen.onkey(p1_paddle_up, 'w')
screen.onkey(p1_paddle_down, 's')
screen.onkey(p2_paddle_up, 'Up')
screen.onkey(p2_paddle_down, 'Down')

ball = Ball()
game_is_on = True
while game_is_on:
    ball.move()
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(p2_paddle) < 40 and ball.xcor() > 450:
        ball.bounce_x()
        ball.speed()
    if ball.distance(p1_paddle) < 40 and ball.xcor() < -450:
        ball.bounce_x()

    # Detect whether ball got out of bounds
    if ball.xcor() > 500:
        ball = Ball()
        ball.x_move *= -1
        ball.y_move *= -1
        p1_score.add_point()

    elif ball.xcor() < -500:
        ball = Ball()
        p2_score.add_point()

screen.exitonclick()
