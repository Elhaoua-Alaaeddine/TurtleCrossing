from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import Car_manager
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("white")
s.title("Turtle Crossing")
s.tracer(0)
s.listen()
p = Player()
score = Scoreboard()
c = Car_manager()
s.onkey(p.move, "w")
done = False
time_add = 0.2
current_time = time.time() + time_add
time_stamp = time.time()
first_loop = True

while not done:
    for car in c.cars:
        if car.distance(p) <= 20:
            score.gameover()
            done = True
            break

    if not time.time() >= time_stamp + 1:
        c.car_speed = 5
        if time.time() >= current_time:
            c.car_spawner()
            current_time = time.time() + time_add

    elif first_loop:
        time_add = 2
        c.car_speed = 0.5
        first_loop = False

    if time.time() >= current_time:
        c.car_spawner()
        current_time = time.time() + time_add

    if p.ycor() >= 160:
        time_add = time_add / 1.5
        score.refresh()
        score.level_up()
        if score.level == 8:
            done = True
            score.win()
            break
        p.refresh()
        c.speed_up()

    c.car_mover()
    s.update()
    time.sleep(0.01)

s.exitonclick()
