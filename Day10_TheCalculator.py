# Functions with Outputs
def my_function():
    results = 3 * 2
    return results

my_function()

# New Exercise
def format_name():
    while True:
        f_name = input("What is your first name: ").strip().title()
        l_name = input("What is your last name: ").strip().title()
        if not f_name or not l_name:
            return "You did not provide valid name, please try again."
        else:
            full_name = f_name + " " + l_name
            return full_name

print(format_name())
#_______________________________________________________________________________________________
# Leap Year Coding Exercise
 
def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
            
is_leap_year(2000)

# Docstrings

def example ():
    print("""When we use a docstring we can write w.e we want,
    skip as many lines as we want and it will be ok!
    It will print when the function is called!""")
    name = input("What is your name?: ").strip().title()
    len= name
    return name and len
example()


#_________________________________________________________________________________________________
# The Calculator Project - Day 10

print("Welcome to the calculator!")
print(''' 
_______________________
|  _________________  |
| |                 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

def my_calculator():
    # Get the first number
    num1 = float(input("What is the first number?: "))
    while True:
        # Ask for operation and second number
        operation = input("Pick an operation: +, -, *, /: ").strip()
        num2 = float(input("What is the next number?: "))
        
        # Perform the calculation
        if operation == "+":
            num1 = num1 + num2
        elif operation == "-":
            num1 = num1 - num2
        elif operation == "*":
            num1 = num1 * num2
        elif operation == "/":
            # Handle division by zero
            if num2 == 0:
                print("Division by zero is not allowed. Try again.")
                continue
            num1 = num1 / num2
        else:
            print("Invalid operation. Please try again.")
            continue
        
        # Print the current result
        print(f"The result is: {num1}")
        
        # Ask if the user wants to continue
        continue_calculating = input("Do you want to continue calculating? Type 'y' for yes or 'n' for no: ").lower()
        if continue_calculating != "y":
            print("Thanks for using the calculator!")
            break

# Run the calculator
my_calculator()