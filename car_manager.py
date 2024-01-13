from turtle import Turtle
import random
import time

CAR_COLORS = ["green", "yellow", "red", "blue", "purple", "orange"]
CAR_STARTING_POSITIONS = [(300, -140), (300, -110), (300, -80), (300, -50), (300, -20), (300, 10), (300, 40),
                          (300, 70), (300, 100), (300, 130)]
CAR_STARTING_SPEED = 0.5
CAR_MOVING_INCREMENT = 0.5


class Car_manager:
    def __init__(self):
        self.cars = []
        self.car_speed = CAR_STARTING_SPEED
        self.car_spawner()

    def car_spawner(self):
        for x in range(10):
            if not random.randint(1, 3) == 1:
                continue
            car = Turtle(shape="square")
            car.shapesize(stretch_len=random.uniform(1.0, 2.0))
            car.color(random.choice(CAR_COLORS))
            car.penup()
            car.ht()
            car.setheading(180)
            car.goto(CAR_STARTING_POSITIONS[x])
            car.showturtle()
            self.cars.append(car)

    def car_mover(self):
        for car in self.cars:
            car.forward(self.car_speed)
            if car.xcor() <= -300:
                car.ht()
                self.cars.remove(car)

    def speed_up(self):
        self.car_speed += CAR_MOVING_INCREMENT
