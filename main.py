import time
from turtle import Screen
from paddle import Paddle
from brick import Bricks
from ball import Ball
from scoreboard import ScoreBoard
import random

# Create screen object
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

# Create paddle objects
paddle = Paddle((0, -300))

# Create 3 rows of block objects
block = Bricks()
new_row = True
while new_row:
    size = random.randint(2, 4)
    new_row = block.extend(size)

# Create scoreboard object
scoreboard = ScoreBoard()

# Create ball
ball = Ball((0, -250))
screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    # Detect collision with wall
    for n in range(len(block.bricks)-1, -1, -1):
        if block.bricks[n].distance(ball) < 50:
            block.bricks[n].hideturtle()
            block.bricks.pop(n)
            if len(block.bricks) == 0:
                scoreboard.win()
                is_game_on = False
            else:
                ball.bounce_y()
    # Detect collision with paddle.
    if ball.distance(paddle) < 55 and ball.ycor() < -275:
        ball.bounce_y()
    # Detect collision with x-axis.
    elif ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()
    # Detect collision with y-axis.
    elif ball.ycor() > 275:
        ball.bounce_y()
    # Detect paddle missed.
    elif ball.ycor() < -275:
        ball.reset_position()
        scoreboard.decrease_score()
        if scoreboard.score == 0:
            is_game_on = False
            scoreboard.gameover()
    time.sleep(ball.move_speed)


screen.exitonclick()