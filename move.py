def move_forwards(snake):
    for segment in snake:
        segment.forward(90)

def move_backwards(snake):
    for segment in snake:
        segment.backward(90)

def turn_left(snake):
    for segment in snake:
        segment.left(90)

def turn_right(snake):
    for segment in snake:
        segment.right(90)

def clear(snake):
    snake.clear()
    snake.penup()
    snake.home()
    snake.pendown()