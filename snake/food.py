from turtle import Turtle
from random import randint

SHAPE = "square"


class Food(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color("blue")
        self.pu()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))

