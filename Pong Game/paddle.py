from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.color("white")

    def move_up(self):
        """Move the paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """Move the paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        """Reset paddle position if out of screen bounds"""
        if self.ycor() > 280:
            self.goto(self.xcor(), 280)
        elif self.ycor() < -280:
            self.goto(self.xcor(), -280)
