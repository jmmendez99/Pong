from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# create objects
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# listening for key presses
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

# game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball will bounce
        ball.bounce_y()

    # Detect collision with right wall
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_score += 1
        scoreboard.update_scoreboard()

    # Detect collision with left wall
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_score += 1
        scoreboard.update_scoreboard()

    # Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320\
            or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()



screen.exitonclick()
