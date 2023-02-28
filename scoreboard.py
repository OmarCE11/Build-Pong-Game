from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 30, 'normal', 'bold')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.points = 0

    def refresh(self):
        self.write(f"{self.points}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.points += 1
        self.clear()
        self.write(f"{self.points}", align=ALIGNMENT, font=FONT)