from turtle import Turtle

STARTING_POSITION = (0, -170)
MOVEMENT = 30


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVEMENT)

    def refresh(self):
        self.speed("fastest")
        self.goto(STARTING_POSITION)
        self.speed("normal")
