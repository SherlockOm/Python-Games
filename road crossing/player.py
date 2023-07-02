from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.shape("turtle")
        self.setheading(90)
        self.back_to_start()

    def back_to_start(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        newx = self.xcor()
        newy = self.ycor() + MOVE_DISTANCE
        self.goto(newx, newy)

    def move_down(self):
        newx = self.xcor()
        newy = self.ycor() - MOVE_DISTANCE
        self.goto(newx, newy)

    def move_left(self):
        newx = self.xcor() - MOVE_DISTANCE
        newy = self.ycor()
        self.goto(newx, newy)

    def move_right(self):
        newx = self.xcor() + MOVE_DISTANCE
        newy = self.ycor()
        self.goto(newx, newy)

