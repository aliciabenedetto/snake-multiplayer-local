import turtle
import time
from sound import play_eat_sound, play_death_sound

from settings import *
from snake import Snake
from food import Food
from score import Scoreboard
from collision import hit_wall, hit_own_body, hit_opponent_body, hit_opponent_head


class Game:
    def __init__(self):
        self.delay = INITIAL_DELAY
        self.state = "menu"

        self.screen = turtle.Screen()
        self.screen.title("Snake Multiplayer Local")
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.tracer(0)

        self.player1 = Snake(PLAYER_1_COLOR, PLAYER_1_START)
        self.player2 = Snake(PLAYER_2_COLOR, PLAYER_2_START)

        self.food = Food()
        self.scoreboard = Scoreboard()

        self.menu_pen = turtle.Turtle()
        self.menu_pen.speed(0)
        self.menu_pen.color("white")
        self.menu_pen.penup()
        self.menu_pen.hideturtle()

        self.hide_game_objects()
        self.setup_controls()
        self.show_menu()

    def setup_controls(self):
        self.screen.listen()

        self.screen.onkey(self.start_game, "Return")
        self.screen.onkey(self.start_game, "KP_Enter")
        self.screen.onkey(self.start_game, "space")
        self.screen.onkey(self.start_game, "p")
        self.screen.onkey(self.start_game, "P")

        self.screen.onkey(self.restart_game, "space")
        self.screen.onkey(self.quit_game, "q")
        self.screen.onkey(self.quit_game, "Q")

        self.screen.onkey(self.player1.go_up, "w")
        self.screen.onkey(self.player1.go_down, "s")
        self.screen.onkey(self.player1.go_left, "a")
        self.screen.onkey(self.player1.go_right, "d")

        self.screen.onkey(self.player1.go_up, "W")
        self.screen.onkey(self.player1.go_down, "S")
        self.screen.onkey(self.player1.go_left, "A")
        self.screen.onkey(self.player1.go_right, "D")

        self.screen.onkey(self.player2.go_up, "Up")
        self.screen.onkey(self.player2.go_down, "Down")
        self.screen.onkey(self.player2.go_left, "Left")
        self.screen.onkey(self.player2.go_right, "Right")

    def hide_game_objects(self):
        self.player1.head.goto(1000, 1000)
        self.player2.head.goto(1000, 1000)
        self.food.position().goto(1000, 1000)

        for segment in self.player1.segments:
            segment.goto(1000, 1000)

        for segment in self.player2.segments:
            segment.goto(1000, 1000)

        self.scoreboard.pen.clear()

    def show_menu(self):
        self.state = "menu"
        self.hide_game_objects()
        self.menu_pen.clear()

        self.menu_pen.goto(0, 120)
        self.menu_pen.write(
            "Players: 2",
            align="center",
            font=("Courier", 20, "normal")
        )

        self.menu_pen.goto(0, 60)
        self.menu_pen.write(
            "Snake Multiplayer Local",
            align="center",
            font=("Courier", 28, "bold")
        )

        self.menu_pen.goto(0, -20)
        self.menu_pen.write(
            "Pressione ESPACO ou P para jogar",
            align="center",
            font=("Courier", 16, "normal")
        )

        self.menu_pen.goto(0, -60)
        self.menu_pen.write(
            "Pressione Q para sair",
            align="center",
            font=("Courier", 16, "normal")
        )

        self.screen.listen()

    def show_game_over(self):
        self.state = "game_over"
        self.hide_game_objects()
        self.menu_pen.clear()

        self.menu_pen.goto(0, 60)
        self.menu_pen.write(
            "GAME OVER",
            align="center",
            font=("Courier", 36, "bold")
        )

        self.menu_pen.goto(0, 10)
        self.menu_pen.write(
            "Fim da rodada multiplayer",
            align="center",
            font=("Courier", 18, "normal")
        )

        self.menu_pen.goto(0, -40)
        self.menu_pen.write(
            "Pressione ESPACO para reiniciar",
            align="center",
            font=("Courier", 16, "normal")
        )

        self.menu_pen.goto(0, -80)
        self.menu_pen.write(
            "Pressione Q para sair",
            align="center",
            font=("Courier", 16, "normal")
        )

        self.screen.listen()

    def start_game(self):
        if self.state == "menu":
            self.state = "playing"
            self.menu_pen.clear()
            self.reset_round()
            self.screen.listen()

    def restart_game(self):
        if self.state == "game_over":
            self.state = "playing"
            self.menu_pen.clear()
            self.reset_round()
            self.screen.listen()

    def quit_game(self):
        self.screen.bye()

    def reset_round(self):
        self.delay = INITIAL_DELAY

        self.player1.reset()
        self.player2.reset()

        self.scoreboard.reset_p1()
        self.scoreboard.reset_p2()
        self.scoreboard.update()

        self.food.random_position()

    def check_food_collision(self):
        food_obj = self.food.position()

        if self.player1.head.distance(food_obj) < 20:
            play_eat_sound()
            self.food.random_position()
            self.player1.grow()
            self.scoreboard.add_p1()
            self.increase_speed()

        if self.player2.head.distance(food_obj) < 20:
            play_eat_sound()
            self.food.random_position()
            self.player2.grow()
            self.scoreboard.add_p2()
            self.increase_speed()

    def increase_speed(self):
        if self.delay > MIN_DELAY:
            self.delay -= SPEED_INCREASE

    def check_death(self):
        player1_dead = (
            hit_wall(self.player1)
            or hit_own_body(self.player1)
            or hit_opponent_body(self.player1, self.player2)
            or hit_opponent_head(self.player1, self.player2)
        )

        player2_dead = (
            hit_wall(self.player2)
            or hit_own_body(self.player2)
            or hit_opponent_body(self.player2, self.player1)
            or hit_opponent_head(self.player2, self.player1)
        )

        if player1_dead or player2_dead:
            play_death_sound()
            time.sleep(0.5)
            self.show_game_over()

    def update_game(self):
        self.check_food_collision()
        self.check_death()

        if self.state != "playing":
            return

        self.player1.move_body()
        self.player2.move_body()

        self.player1.move()
        self.player2.move()

    def run(self):
        while True:
            self.screen.update()

            if self.state == "playing":
                self.update_game()

            time.sleep(self.delay)
            