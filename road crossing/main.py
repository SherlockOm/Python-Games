import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)


player = Player()

screen.listen()
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "s")
screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")

scoreboard = Scoreboard()

car = CarManager()

TIME = 0.1
game_is_on = True
while game_is_on:
    time.sleep(TIME)
    car.create_car()
    car.move()
    if player.ycor() > 280:
        scoreboard.inc_level()
        TIME *= 0.9
        player.back_to_start()

    for vehicle in car.cars:
        if player.distance(vehicle) < 25:
            scoreboard.game_over()
            game_is_on = False
        elif abs(vehicle.xcor() - player.xcor()) < 35 and abs(vehicle.ycor() - player.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False

    screen.update()

screen.exitonclick()