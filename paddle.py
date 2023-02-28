from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('rectangle')
        self.color('white')
        self.setheading(90)