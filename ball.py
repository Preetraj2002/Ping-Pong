from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setheading(45)
        self.move_speed=0.02

    def move(self):

        self.forward(6)


    def bounce(self):
        self.setheading(360-self.heading())

    def bounce_with_paddle(self):
        self.move_speed*=0.95
        self.setheading(180-self.heading())
        self.forward(30)

    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.02
        self.setheading(self.heading()+270)