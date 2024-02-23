def move_forwards(snake):
    snake.forward(10)

def move_backwards(snake):
    snake.backward(10)

def turn_left(snake):
    snake.left(10)

def turn_right(snake):
    snake.right(10)

def clear(snake):
    snake.clear()
    snake.penup()
    snake.home()
    snake.pendown()