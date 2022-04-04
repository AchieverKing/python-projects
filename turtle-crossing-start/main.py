import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car = CarManager()
score = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Cross Game")
screen.tracer(0)
screen.listen()
screen.onkey(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    """detect collision of turtle with car"""
    for i in car.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            score.game_over()

    """detect if the player has reached the other side"""
    if player.is_at_finish_line():
        player.go_to_start()
        score.increase_score()
        car.level_up()


screen.exitonclick()
