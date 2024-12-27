# Subscription
print("Hello" [4])

# String, QUOTATION MARKS makes them a string!
print("123" + "345")

# Integer = Whole number
print(123+345)

# Large Integers (The underscore makes it more readable, can also be a comma)
print(123_456_789)

# Float = Floating Point Number (Any Decimal point!)
print(3.14159)

# Boolean
print(True)
print(False)

# len
len("12345")

# By using type(), you can figure out the data type of any piece of data
print(type("Hello"))
print(type(123456))
print(type(123_456.789))
print(type(True))

# Conversion
print(int("123")+int("456"))

int()
float()
str()
bool()

print("Number of letters in your nmme:" + str(len(input("Enter your name"))))

# PERMDAS ORDER from LEFT to RIGHT
# ()
# **
# * or /
# + or -
print(3*(3+3)/3-3)

# Print the BMI of a person

height = 5.2 * 0.3048 # Converting foot to meters
weight = 110 * 0.453592 # Converting kilograms to pounds
bmi = weight / (height**2)

print(round(bmi,2))

# f-String
score = 1
height = 1.8
is_winning = True
print (f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

# Project: Tip Calculator

#Greetings
print("Welcome to the tip calculator!")
total_bill = float(input("Enter the total bill amount. $"))
tips = int(input("Choose a tip percentage (10,12,15):"))
people = int(input("How many people should split the bill?"))
each = round(((total_bill*(1+tips/100)/people)),2)

print((f"Each person should pay = ${each}"))