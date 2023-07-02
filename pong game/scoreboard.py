from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1 = 0
        self.player2 = 0
        self.color("LawnGreen")
        self.pu()
        self.hideturtle()
        self.partition_line()

    def partition_line(self):
        self.goto(0, -230)
        self.setheading(90)
        while self.ycor() < 230.0:
            self.pu()
            self.fd(10)
            self.pd()
            self.fd(10)
        self.pu()
        self.bk(20)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.player1}   {self.player2}",align="center",font=("Arial",24,"bold"))

    def inc_score(self):
        self.clear()
        self.partition_line()
