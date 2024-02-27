"""_summary_
+ First 3 Steps:
- Create the body of the snake
- Move the snake
- Control the snake

+ Second 4 steps:
- Detect collision with food
- Create a scoreboard
- Detect collision with a wall (The game should end)
- Detect collision with tail (The game should end)
"""

from turtle import Screen, Turtle
from move import move_forwards, move_backwards, turn_left, turn_right, clear

import time

screen = Screen()
snake = []
speed = 1
angles = [90, 180, 270, 360]


def setup():
    screen.title("Snake Game")
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    # screen.listen()
    screen.tracer(0)

# 1st step
def create_snake():
    for index in range(3):
        segment = Turtle("square")
        segment.penup()
        segment.resizemode("user")
        segment.shapesize(0.5, 0.5)
        segment.color("white")
        # segment.speed(speed)
        if snake:
            # print(f"xcor: {xcor}", f"ycor: {ycor}")
            segment.backward(10 * index)
        snake.append(segment)

# 2nd step
def move_snake():
    print(snake)
    screen.onkey(key="w", fun=lambda snake=snake: move_forwards(snake))
    screen.onkey(key="s", fun=lambda snake=snake: move_backwards(snake))
    screen.onkey(key="a", fun=lambda snake=snake: turn_left(snake))
    screen.onkey(key="d", fun=lambda snake=snake: turn_right(snake))
    screen.onkey(key="c", fun=lambda snake=snake: clear(snake))


setup()
create_snake()
# move_snake()

on = True
while on:
    screen.update()
    time.sleep(0.1)
    for seg_index in range(len(snake) - 1, 0, -1):
        new_x = snake[seg_index - 1].xcor()
        new_y = snake[seg_index - 1].ycor()
        snake[seg_index].goto(new_x, new_y)
    snake[0].forward(10)
    # segments[0]


# print("\n")
# print(snake_body)
# for snake in snake_body:
#     print(snake.xcor(), snake.ycor())

screen.exitonclick()
