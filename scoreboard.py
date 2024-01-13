from turtle import Turtle
import random

CONGS = ["Well Done!", "Nice!", "Keep it up!", "( ͡° ͜ʖ ͡°)"]


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("black")
        self.goto(-290, 260)
        self.level = 1
        self.write_level()

    def refresh(self):
        self.level += 1
        self.clear()
        self.write_level()

    def write_level(self):
        self.goto(-290, 260)
        self.write(arg=f"Level: {self.level}", align="left", font=("Arial", 15, "bold"))

    def gameover(self):
        self.goto(0, 200)
        self.write(arg="Game Over", align="center", font=("Arial", 20, "bold"))

    def level_up(self):
        self.goto(0, 0)
        self.write(arg=random.choice(CONGS), align="center", font=("Arial", 20, "bold"))

    def win(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="You Win!", align="center", font=("Arial", 20, "bold"))