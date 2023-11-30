from turtle import Turtle, Screen
from label import Label
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.tracer(0)

screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("PONG")

r_label = Label((270, 0))
l_label = Label((-270, 0))
middle = Label((5, 280))
my_ball = Ball()
scoreboard = ScoreBoard()
middle.dashed_line()

screen.listen()
screen.onkey(fun=l_label.Up, key="w")
screen.onkey(fun=l_label.Down, key="s")
screen.onkey(fun=r_label.Up, key="Up")
screen.onkey(fun=r_label.Down, key="Down")

is_game_on = True
while is_game_on:
    screen.update()
    scoreboard.update_scoreboard()
    time.sleep(my_ball.move_speed)
    my_ball.move()
    if my_ball.xcor() > 280:
        scoreboard.increase_left_score()
        my_ball.reset_position()
        scoreboard.update_scoreboard()
    elif my_ball.xcor() < -280:
        scoreboard.increase_right_score()
        my_ball.reset_position()
        scoreboard.update_scoreboard()
    if my_ball.ycor() > 270 or my_ball.ycor() < -270:
        my_ball.y_bounce()
    if my_ball.distance(l_label) < 50 and my_ball.xcor() <-260:
        my_ball.x_bounce()
    if my_ball.distance(r_label) < 50 and my_ball.xcor() > 260:
        my_ball.x_bounce()
    if scoreboard.score2 == 3 or scoreboard.score1 == 3:
        turtle = Turtle()
        turtle.color("white")
        turtle.write("GAME OVER", False, "center", ("Times New Roman", 40, "normal"))
        turtle.penup()
        turtle.goto(0, -50)
        if scoreboard.score1 == 3:
            turtle.write("The left player has won", False, "center", ("Courier", 24, "normal"))
        elif scoreboard.score2 == 3:
            turtle.write("The right player has won", False, "center", ("Courier", 24, "normal"))
        is_game_on = False




screen.exitonclick()

