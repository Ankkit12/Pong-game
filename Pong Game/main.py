from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

"""This is screen setup"""
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
screen.listen()

"""This is paddle setup"""
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))


# left_out = l_paddle.paddle_out_of_screen()
# right_out = r_paddle.paddle_out_of_screen()


screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = Ball()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.moving_ball()
    scoreboard.update_score()

    # Detect the collision with the wall and trigger move down
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # See if ball goes out of bounds and then reset the game
    if ball.xcor() > 380:
        scoreboard.update_l_score()
        ball.restart()

    if ball.xcor() < -380:
        scoreboard.update_r_score()
        ball.restart()

    # Update paddles in the game loop
    l_paddle.reset_position()
    r_paddle.reset_position()

screen.exitonclick()
