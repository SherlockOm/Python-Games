from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.xmove = 10
        self.ymove = 10

    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx, newy)

    def reflect_walls(self):
        self.ymove *= -1

    def reflect_board(self):
        self.xmove *= -1
