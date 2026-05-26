from settings import BOUNDARY


def hit_wall(snake):
    x = snake.head.xcor()
    y = snake.head.ycor()

    return x > BOUNDARY or x < -BOUNDARY or y > BOUNDARY or y < -BOUNDARY


def hit_own_body(snake):
    for segment in snake.segments:
        if snake.head.distance(segment) < 20:
            return True
    return False


def hit_opponent_body(snake, opponent):
    for segment in opponent.segments:
        if snake.head.distance(segment) < 20:
            return True
    return False


def hit_opponent_head(snake, opponent):
    return snake.head.distance(opponent.head) < 20
