from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        num = randint(1,6)
        if num == 1:
            new_car = Turtle()
            rand_y = randint(-250,250)
            new_car.goto(300,rand_y)
            new_car.penup()
            new_car.shape("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.bk(STARTING_MOVE_DISTANCE)
