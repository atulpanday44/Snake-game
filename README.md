🐍 Classic Snake Game
This project is a simple implementation of the Classic Snake Arcade Game using Python and the turtle module. It also utilizes a helper from the freegames library to simplify graphics rendering.

🎮 Gameplay
Control a snake using the arrow keys.

Eat the green square (food) to grow in size.

Avoid colliding with the walls or the snake's own body.

The game ends if the snake hits the wall or itself.

🧾 Code Overview
Main Components:
snake: A list of vector objects representing the segments of the snake.

food: A vector representing the food's position.

aim: A vector indicating the current movement direction of the snake.

Key Functions:
change(x, y): Updates the aim direction.

inside(head): Checks if the snake's head is within game boundaries.

move(): Main game loop:

Moves the snake in the current direction.

Checks for collisions.

Handles food consumption and growth.

Updates the screen.

📝 Exercises & Enhancements
Here are some suggested exercises to expand the game functionality:

1. 🐇 How do you make the snake faster or slower?
Adjust the timer interval in the ontimer(move, 100) call:

python
Copy code
ontimer(move, 100)  # Lower is faster (e.g., 50), higher is slower (e.g., 150)
2. 🌍 How can you make the snake go around the edges?
Modify the inside() function to allow the snake to wrap around:

python
Copy code
def inside(head):
    head.x = (head.x + 200) % 400 - 200
    head.y = (head.y + 200) % 400 - 200
    return True
Or handle this logic in the move() function by checking edges and wrapping the coordinates.

3. 🍏 How would you move the food?
You can make the food move randomly by adding:

python
Copy code
def move_food():
    food.move(vector(randrange(-1, 2) * 10, randrange(-1, 2) * 10))
    if not inside(food):  # Keep it within bounds
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    ontimer(move_food, 1000)

move_food()
4. ⌨️ Change the snake to respond to arrow keys
This is already implemented in the code using:

python
Copy code
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
You can modify or add support for WASD or other input schemes similarly.

▶️ How to Run
Install Python (version 3.6+ recommended).

Install freegames if not already installed:

bash
Copy code
pip install freegames
Run the game:

bash
Copy code
python snake.py
🧠 Requirements
Python 3.x

freegames module

turtle module (comes with Python standard library)
