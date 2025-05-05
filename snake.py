from turtle import *
from random import randrange
from freegames import square, vector

# Initial positions and directions
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Game speed (lower is faster)
SPEED = 100  # Change to 50 or 150 for faster/slower

# Edge wrapping mode (set to True for wrapping, False for solid borders)
WRAP_EDGES = False

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries, or wrap if enabled."
    if WRAP_EDGES:
        head.x = (head.x + 200) % 400 - 200
        head.y = (head.y + 200) % 400 - 200
        return True
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or (not WRAP_EDGES and head in snake):
        square(head.x, head.y, 9, 'red')
        update()
        return

    # In wrapping mode, avoid killing self on wrapped coordinate
    if WRAP_EDGES and head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        move_food()
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, SPEED)

def move_food():
    "Randomly move food one step in any direction."
    food_move = vector(randrange(-1, 2) * 10, randrange(-1, 2) * 10)
    food.move(food_move)
    if not inside(food):
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

# Set up game window
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Arrow key bindings
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
