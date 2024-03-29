from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen=Screen()
screen.setup(900,600)
screen.bgcolor("black")
screen.title("my pong game")
screen.tracer(0)

paddle_r=Paddle(420,0)
paddle_l=Paddle(-420,0)
ball=Ball()
score=Scoreboard()


screen.listen()
screen.onkey(paddle_r.move_up,"Up")
screen.onkey(paddle_r.move_down,"Down")
screen.onkey(paddle_l.move_up,"w")
screen.onkey(paddle_l.move_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.moveBall()
    if ball.ycor() >= 280 or ball.ycor()<=-280:#detect collision with the top and bottom borders
        ball.changePosVertical()
    if ball.distance(paddle_r)<50 and ball.xcor()>400 or ball.distance(paddle_l)<50 and ball.xcor()<-400:
        print("made contact")
        ball.changePosHorizontal()#made contact with the paddle on right and left

    if ball.xcor()>420:
        ball.reset_position()
        ball.changePosHorizontal()
        score.clear()
        score.increaseScore_l()
    if ball.xcor()<-420:
        ball.reset_position()
        ball.changePosHorizontal()
        score.clear()
        score.increaseScore_r()


screen.exitonclick()