from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        self.x_move=10
        self.y_move=10
        super().__init__()
        self.createBall()
        self.move_speed=0
    def createBall(self):
        self.color("white")
        self.shape("circle")
        self.setpos(0,0)

    def moveBall(self):
        self.penup()
        x_cor=self.xcor()+self.x_move
        y_cor=self.ycor()+self.y_move
        self.goto(x_cor,y_cor)
        print(x_cor,y_cor)

    def changePosVertical(self):
        self.y_move*=-1  #y_move is 10 now, it will be -10

    def changePosHorizontal(self):
        self.x_move*=-1  #x_move is 10 now, it will be -10
        self.move_speed*=0.9

    def reset_position(self):
        self.move_speed=0.1
        self.goto(0,0)