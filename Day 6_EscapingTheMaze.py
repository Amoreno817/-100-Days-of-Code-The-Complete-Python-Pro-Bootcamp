# Functions, Code Blocks & While Loops

num_char = len("Hello")
print(num_char)

def my_function():
    print("Hello")
    print("Bye")

my_function()
# 1) Define the function first, then call it. Whatever is in the line of code under the 
# function will trigger. Be sure to add the "():" and indent
#_____________________________________________________________________________________________
# Karel the robot
# def turn_around():
#     turn_left()
#     turn_left()
    
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    # for step in range(6):
#     jump()
#_________________________________________________________________________________________________
chocolates = ['milk', 'dark', 'white']

# Using 'chocolate' as the loop variable
for chocolate in chocolates:
    print(chocolate)

# Using 'item' as the loop variable
for item in chocolates:
    print(item)

# Using 'x' as the loop variable
for x in chocolates:
    print(x)

#__________________________________________________________________________________________________
# Indentation
def la_function(): # You can think of this like a folder, and the content below is in the folder.
    print("Hola") # This is inside the folder

print("Hello") # This is outside the "folder", and therefore not part of the above function.
la_function()

#__________________________________________________________________________________________________
# Loops (Iteration?)
# Real-World Analogy
# Imagine you're reading a book:

# The loop is the process of flipping through each page (the repeating action).
# Each iteration is reading one page.
# You can’t have a loop without iterations, 
# just like you can’t flip through a book without going page by page.

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:  # The loop
    print(fruit)      # The action during each iteration

# Output
# apple  # First iteration
# banana # Second iteration
# cherry # Third iteration

#_______________________________________________________________________________________________
# While Loop

power_level = 10000
while power_level > 9000:
    power_level -= 100
    print("Is over NINE THOUSANDS!")

# Escape the maze
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
