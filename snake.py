import turtle
from settings import STEP


class Snake:
    def __init__(self, color, start_position):
        self.color = color
        self.start_position = start_position
        self.direction = "stop"
        self.segments = []

        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color(color)
        self.head.penup()
        self.head.goto(start_position)

    def go_up(self):
        if self.direction != "down":
            self.direction = "up"

    def go_down(self):
        if self.direction != "up":
            self.direction = "down"

    def go_left(self):
        if self.direction != "right":
            self.direction = "left"

    def go_right(self):
        if self.direction != "left":
            self.direction = "right"

    def move(self):
        x = self.head.xcor()
        y = self.head.ycor()

        if self.direction == "up":
            self.head.sety(y + STEP)
        elif self.direction == "down":
            self.head.sety(y - STEP)
        elif self.direction == "left":
            self.head.setx(x - STEP)
        elif self.direction == "right":
            self.head.setx(x + STEP)

    def grow(self):
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color(self.color)
        segment.penup()
        segment.goto(1000, 1000)
        self.segments.append(segment)

    def move_body(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)

        if len(self.segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x, y)

    def reset(self):
        self.head.goto(self.start_position)
        self.direction = "stop"

        for segment in self.segments:
            segment.goto(1000, 1000)

        self.segments.clear()
        