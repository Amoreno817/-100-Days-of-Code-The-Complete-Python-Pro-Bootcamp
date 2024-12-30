# For Loop = for item in list_of_items: Do something for each item 

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print (fruit)
    print (fruit + " pie")

#________________________________________________________________________________________

# Highest Score

student_scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

#________________________________________________________________________________________
# For loop with range function

# Note: By itself, the range() function doesn't do anything,
#       it must be used in conjuction with another function.

total = 0
for number in range(1,101):
   total += number
   
print (total)

# Challenge: Your program should print each number from 1 to 100 in turn 
# and include number 100. But when the number is divisible by 3 then instead 
# of printing the number it should print "Fizz". When the number is divisible
# by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the 
# number it should print "FizzBuzz"

for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print ("FizzBuzz")
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print ("Buzz")
    else:
        print (number)

# Password Genrator

print (''' 

    .--------.
    / .------. 
   / /        \ 
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  |      |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'
''' )

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
password_generator = []

for char in range (0, nr_letters):
   password_generator += random.choice (letters)

for char in range(0, nr_symbols):
    password_generator += random.choice (symbols)

for char in range(0, nr_numbers):
    password_generator += random.choice(numbers)

#Hard Level - Order of characters randomised:
random.shuffle(password_generator)
password = ''.join(password_generator)
print(f"Your password is: {password}")