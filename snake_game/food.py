import random
from turtle import Turtle
class Food:
    def __init__(self):
        self.food = Turtle()
        self.create_food()
        self.food_x = 0
        self.food_y = 0

    def create_food(self):
        self.food.hideturtle()
        self.food_x = random.randrange(-270, 270)
        self.food_y = random.randrange(-270, 270)
        self.food.shape('circle')
        self.food.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.food.color('red')
        self.food.penup()
        self.food.goto(self.food_x, self.food_y)
        self.food.showturtle()

    def snake_ate_food(self,head_position):
        if self.food.distance(head_position) < 15:
            self.create_food()
            return True
        else:
            return False




