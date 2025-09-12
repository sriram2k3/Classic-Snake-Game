from turtle import Screen
from Snake import Snake
from food import Food
import time

from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# main code
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    if snake.move():
        scoreboard.reset_score()
        snake = Snake()
        screen.onkey(snake.snake_up, "Up")
        screen.onkey(snake.snake_down, "Down")
        screen.onkey(snake.snake_left, "Left")
        screen.onkey(snake.snake_right, "Right")
    if food.snake_ate_food(snake.squares[0]):
        scoreboard.increase_score()
        snake.add_segment()

screen.exitonclick()
