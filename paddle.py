from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.create_paddle(x,y)
    def create_paddle(self,x,y):
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.setpos(x,y)

    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
