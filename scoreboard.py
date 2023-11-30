from turtle import Turtle, Screen


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")

    def update_scoreboard(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-70, 240)
        self.write(self.score1, False, "center", ("Courier", 30, "normal"))
        self.goto(60, 240)
        self.write(self.score2, False, "center", ("Courier", 30, "normal"))

    def increase_left_score(self):
        self.score1 += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.score2 += 1
        self.update_scoreboard()
