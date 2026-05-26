import turtle
import time

from settings import *
from snake import Snake
from food import Food
from score import Scoreboard
from collision import hit_wall, hit_own_body, hit_opponent_body, hit_opponent_head


class Game:
    def __init__(self):
        self.delay = INITIAL_DELAY

        self.screen = turtle.Screen()
        self.screen.title("Snake Multiplayer Local")
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.tracer(0)

        self.player1 = Snake(PLAYER_1_COLOR, PLAYER_1_START)
        self.player2 = Snake(PLAYER_2_COLOR, PLAYER_2_START)

        self.food = Food()
        self.scoreboard = Scoreboard()

        self.setup_controls()

    def setup_controls(self):
        self.screen.listen()

        self.screen.onkeypress(self.player1.go_up, "w")
        self.screen.onkeypress(self.player1.go_down, "s")
        self.screen.onkeypress(self.player1.go_left, "a")
        self.screen.onkeypress(self.player1.go_right, "d")

        self.screen.onkeypress(self.player2.go_up, "Up")
        self.screen.onkeypress(self.player2.go_down, "Down")
        self.screen.onkeypress(self.player2.go_left, "Left")
        self.screen.onkeypress(self.player2.go_right, "Right")

    def check_food_collision(self):
        food_obj = self.food.position()

        if self.player1.head.distance(food_obj) < 20:
            self.food.random_position()
            self.player1.grow()
            self.scoreboard.add_p1()
            self.increase_speed()

        if self.player2.head.distance(food_obj) < 20:
            self.food.random_position()
            self.player2.grow()
            self.scoreboard.add_p2()
            self.increase_speed()

    def increase_speed(self):
        if self.delay > MIN_DELAY:
            self.delay -= SPEED_INCREASE

    def check_death(self):
        if (
            hit_wall(self.player1)
            or hit_own_body(self.player1)
            or hit_opponent_body(self.player1, self.player2)
            or hit_opponent_head(self.player1, self.player2)
        ):
            time.sleep(0.5)
            self.player1.reset()
            self.scoreboard.reset_p1()
            self.delay = INITIAL_DELAY

        if (
            hit_wall(self.player2)
            or hit_own_body(self.player2)
            or hit_opponent_body(self.player2, self.player1)
            or hit_opponent_head(self.player2, self.player1)
        ):
            time.sleep(0.5)
            self.player2.reset()
            self.scoreboard.reset_p2()
            self.delay = INITIAL_DELAY

    def run(self):
        while True:
            self.screen.update()

            self.check_food_collision()
            self.check_death()

            self.player1.move_body()
            self.player2.move_body()

            self.player1.move()
            self.player2.move()

            time.sleep(self.delay)
            