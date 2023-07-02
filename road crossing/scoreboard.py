from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("white")
        self.level = 0
        self.goto(-200, 260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def inc_level(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.goto(0,-90)
        self.pd()
        self.circle(100)
        self.pu()
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=FONT)

