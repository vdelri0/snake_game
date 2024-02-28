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
from snake import Snake
from turtle import Screen, Turtle

import time

ON = True
SPEED = 1
SLEEP = 0.1 # How fast the snake is going to move

class main():
    def __init__(self):
        self.snake = Snake()
        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkey(self.snake.up, "w")
        self.screen.onkey(self.snake.down, "s")
        self.screen.onkey(self.snake.left, "a")
        self.screen.onkey(self.snake.right, "d")

        while ON:
            self.screen.update()
            time.sleep(SLEEP)
            self.snake.move()
            self.snake
        self.screen.exitonclick()

if __name__ == '__main__':
    main = main()

# print("\n")
# print(snake_body)
# for snake in snake_body:
#     print(snake.xcor(), snake.ycor())
