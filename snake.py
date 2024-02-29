from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    # 1st step
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.resizemode("user")
        segment.color("white")
        segment.shapesize(0.5, 0.5)
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def extend(self):
        """Add a new segment to the snake"""
        self.add_segment(self.snake[-1].position())

    # 2nd step
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def clear(self):
        self.snake.clear()
        self.snake.penup()
        self.snake.home()
        self.snake.pendown()

    def move(self):
        for seg_index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_index - 1].xcor()
            new_y = self.snake[seg_index - 1].ycor()
            self.snake[seg_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        # snake[0].left(90)
