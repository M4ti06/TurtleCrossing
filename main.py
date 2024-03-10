import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move,"Up")

counter = 0
game_is_on = True
while game_is_on:
    counter += 1
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.moving_cars()
    for car in car_manager.all_cars:
        if player.distance(car) < 20 :
            scoreboard.game_over()
            game_is_on = False
    if player.is_at_finishing_line():
        player.reset()
        car_manager.level_up()
        scoreboard.next_level()


screen.exitonclick()