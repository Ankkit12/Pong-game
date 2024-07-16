from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def moving_ball(self):
        """This function moves the ball"""
        x_cor = self.xcor() + self.move_x
        y_cor = self.ycor() + self.move_y
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        """This function bounces the ball from origin when hit with wall"""
        self.move_y *= -1

    def bounce_x(self):
        """This function bounces the ball along x-axis """
        self.move_x *= -1
        self.move_speed *= 0.9

    def restart(self):
        """This function puts the ball in origin"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()




