import turtle as t
import paddle
import ball
import time
from scoreboard import Scoreboard

screen = t.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("My ping pong game")

screen.tracer(0)

r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
ball = ball.Ball()
scoreboard1 = Scoreboard()

# ceiling = t.Turtle()
# ceiling.sety(300)
# ceiling.shapesize(stretch_len=100, stretch_wid=0.5)
# ceiling.color("white")
# ceiling.shape("square")


screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")


def exitprogram():
    screen.bye()


screen.onkeypress(exitprogram, "Escape")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    print(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 430:
        scoreboard1.l_points()
        ball.restart()
    if ball.xcor() < -430:
        scoreboard1.r_points()
        ball.restart()

screen.exitonclick()
