from turtle import Screen, Turtle
from scoreboard import Scoreboard
from board import Board
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 500)
screen.tracer(0)

scoreboard = Scoreboard()
scoreboard.partition_line()

board1 = Board(-380)
board2 = Board(375)

screen.listen()
screen.onkeypress(board1.move_up, "w")
screen.onkeypress(board1.move_down, "s")
screen.onkeypress(board2.move_up, "Up")
screen.onkeypress(board2.move_down, "Down")

ball = Ball()

Time = 0.1
game_on = True
while game_on:
    time.sleep(Time)
    if scoreboard.player1 == 10 or scoreboard.player2 == 10:
        if scoreboard.player1 == 10 :
            scoreboard.write("Player 1 wins !game over", align="center", font=("Arial", 24, "bold"))
        else :
            scoreboard.write("Player 2 wins !game over", align="center", font=("Arial", 24, "bold"))
        scoreboard.clear()
        scoreboard.home()
        game_on = False
    if ball.xcor() > 360 or ball.xcor() < -360:
        if ball.xcor() > 0: scoreboard.player1 += 1
        else: scoreboard.player2 += 1
        scoreboard.inc_score()
        Time = 0.1
        ball.home()
        ball.xmove *= -1
    if ball.ycor() >= 225 or ball.ycor() <= -225:
        ball.reflect_walls()
    if ball.distance(board1) < 50 and ball.xcor() < -350 \
    or ball.distance(board2) < 50 and ball.xcor() > 350:
        ball.reflect_board()
        Time *= 0.9

    ball.move()
    screen.update()

screen.exitonclick()
