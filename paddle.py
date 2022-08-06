from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, pos):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(pos)

    def up(self):
        if self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + 25)

    def down(self):
        if self.ycor() > -260:
            self.goto(self.xcor(), self.ycor() - 25)



