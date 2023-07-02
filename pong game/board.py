from turtle import Turtle


class Board(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("cyan")
        self.pu()
        self.shape("square")
        self.goto(position, 0)
        self.shapesize(stretch_wid=5, stretch_len=0.5)

    def move_up(self):
        if self.ycor() < 200:
            ycord = self.ycor() + 20
            self.goto(self.xcor(), ycord)

    def move_down(self):
        if self.ycor() > -200:
            ycord = self.ycor() - 20
            self.goto(self.xcor(), ycord)
