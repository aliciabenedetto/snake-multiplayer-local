import turtle
import random


class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.random_position()

    def random_position(self):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.food.goto(x, y)

    def position(self):
        return self.food
    