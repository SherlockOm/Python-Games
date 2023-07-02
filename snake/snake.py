from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SHAPE = "circle"


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("red")

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle(SHAPE)
        new_segment.shapesize(stretch_len=0.7,stretch_wid=0.7)
        new_segment.pu()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[segment - 1].xcor()
            newy = self.segments[segment - 1].ycor()
            self.segments[segment].goto(newx, newy)
        self.head.fd(20)

    def up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
