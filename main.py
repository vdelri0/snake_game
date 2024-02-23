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

screen = Screen()

def setup():
    screen.title("Snake Game")
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.listen()

# 1st step
snake_body = []

def create_snake():
    for index in range(3):
        snake = Turtle("square")
        snake.shapesize(0.5, 0.5)
        snake.color("white")
        if snake_body:
            # print(f"xcor: {xcor}", f"ycor: {ycor}")
            snake.backward(10 * index)
        snake_body.append(snake)

# 2nd step
def move_snake():
    print(snake_body)
    for snake in snake_body:
        screen.onkey(key="w", fun=lambda snake=snake: move_forwards(snake))
        screen.onkey(key="s", fun=lambda snake=snake: move_backwards(snake))
        screen.onkey(key="a", fun=lambda snake=snake: turn_left(snake))
        screen.onkey(key="d", fun=lambda snake=snake: turn_right(snake))
        screen.onkey(key="c", fun=lambda snake=snake: clear(snake))

setup()
create_snake()
move_snake()

# print("\n")
# print(snake_body)
# for snake in snake_body:
#     print(snake.xcor(), snake.ycor())

screen.exitonclick()
