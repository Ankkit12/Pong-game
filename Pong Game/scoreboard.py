from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()

    def update_score(self):
        """This function shows the scores of the both the paddles"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=('Courier', 80, 'normal'))

    def update_l_score(self):
        """This function updates the score of the left paddle"""
        self.l_score += 1
        self.update_score()

    def update_r_score(self):
        """This function updates the score of right paddle"""
        self.r_score += 1
        self.update_score()
