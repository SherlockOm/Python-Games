import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = t.Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

food = Food()
scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.125)
    snake.move()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_on = False
            scoreboard.game_over()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.inc_score()
        snake.extend()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290\
    or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()

screen.exitonclick()
