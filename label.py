from turtle import Turtle


class Label(Turtle):
    def __init__(self, given_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed(0)
        self.penup()
        self.position = given_position
        self.goto(given_position)

    def Up(self):
        if self.ycor() < 240:
            new_y = self.ycor() +40
            self.goto(self.xcor(), new_y)

    def Down(self):
        if self.ycor() > -240:
            new_y = self.ycor() -40
            self.goto(self.xcor(), new_y)

    def dashed_line(self):
        self.color("white")
        self.setheading(270)
        self.hideturtle()
        self.penup()
        self.goto(self.position)
        while self.ycor() > -280:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
