import turtle


class Scoreboard:
    def __init__(self):
        self.score_p1 = 0
        self.score_p2 = 0

        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)

        self.update()

    def update(self):
        self.pen.clear()
        self.pen.write(
            f"Jogador 1: {self.score_p1}    Jogador 2: {self.score_p2}",
            align="center",
            font=("Courier", 18, "normal")
        )

    def add_p1(self):
        self.score_p1 += 10
        self.update()

    def add_p2(self):
        self.score_p2 += 10
        self.update()

    def reset_p1(self):
        self.score_p1 = 0
        self.update()

    def reset_p2(self):
        self.score_p2 = 0
        self.update()
        