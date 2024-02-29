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
from food import Food
from scoreboard import Scoreboard
from turtle import Screen

import time

ON = True
SPEED = 1
SLEEP = 0.1 # How fast the snake is going to move

class main():
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
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

            # Detect collision with food
            if self.snake.head.distance(self.food) < 15:
                self.food.refresh()
                self.snake.extend()
                self.scoreboard.increase_score()

            # Detect collision with wall
            if self.snake.head.xcor() > 280 or self.snake.head.xcor() < -280 or self.snake.head.ycor() > 280 or self.snake.head.ycor() < -280:
                self.game_over()

            # Detect collision with tail
            for segment in self.snake.snake[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.game_over()

        self.screen.exitonclick()

    def game_over(self):
        global ON
        ON = False
        self.scoreboard.game_over()

if __name__ == '__main__':
    main = main()
