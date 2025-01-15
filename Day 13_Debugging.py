# Day 13_Debugging

# Warm up: Broken Code w/ ChatGPT
def calculate_average(numbers):
    total = 0
    for num in numbers:  # Typo here
        total += num
    if len(numbers) == 0:  # Check for an empty list
        print("The list is empty, cannot calculate the average.")
        return
    if any(num <= 0 for num in numbers):
        print("Your number can't be less than or equal to zero.")
        return
    avg = total / len(numbers) # Division by zero possibility
   
    print(f"The average is:{avg}")  # TypeError: Can't concatenate str and float

# Test the function
my_numbers = [10, 20, 30]
calculate_average(my_numbers)

#__________________________________________________________________________________________
# Debugging the first problem

def my_function():
    for i in range(1,21): # Remember a range of range(1,20) only loops through 1-19, change it to (1,21)
        if i == 20:
            print ("You got it!")

my_function()

#________________________________________________________________________________________________
# Debuggging the second problem
from random import randint
dice_images = ["1","2","3","4","5","6"] # Remember the index starts at 0 and works up in the list. 6 is out of range
dice_num = randint(0, 5)
print(dice_images[dice_num])

#_________________________________________________________________________________________________
# Debugging lessons continues: Play Computer

year = int(input("What's your year of birth?"))

if year > 1990 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a GenZ.")

# Fixing the erros
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical number.")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can now drive at age {age}.")
else:
    print("YOU CAN'T DRIVE YET!")

# Print is Your Friend, print out each variable to narrow out the cause of the issue, see if
# ypu get the desired outcome.

# Debugging tips
# 1- Take a break
# 2- Ask a friend (discord)
# 3- Run your code often so that you can catch the mistake early
# 4 - Stack Overflow: ask questions last alternative ; Plan Z

#__________________________________________________________________________________
# Debugging Problems

# 1 Odd or Even?
def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
        
odd_or_even(1)

#2 is_leap year

def is_leap(year):
    if year == 2000:
        return True
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

is_leap(2000)

#3 FizzBuzz
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
            
fizz_buzz(15)
