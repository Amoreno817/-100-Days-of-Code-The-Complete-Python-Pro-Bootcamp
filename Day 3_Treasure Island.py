# Condition IF/ELSE
print("Welome to the rollarcoaster!")
height = int(input("What is your height in centimeters?"))
bill = 0

if height >= 120:
        print("You can ride the rollercoaster!")
        age = int(input("What is your age"))
        if age <= 12:
               bill = 5
               print ("Child tickets are $5")
        elif age <= 18:
                bill = 7 
                print("Youth tickets are $7")
        else:
               bill = 12
               print ("Adult tickets are $12.")
        if age > 44 and age < 56:
               bill = 0
               print ("Your ticket is $0") 
        
        want_photo = input("Would you like to include a photo with the tickets?" "yes or no")
        if want_photo == "yes":
            bill += 3
        print (f"Your total is $ {bill}") 
        if want_photo == "no":
            print (f"Your total is $ {bill}")
else:
        print("Sorry, you have to grow taller before you can ride.")

#____________________________________________________________________________________________

# Comparison Operators
    # >   Greater than
    # <   Less than
    # >=  Greater than or equal to
    # <=  Less than or equal to
    # ==  Equal to
    # !=  Not Equal to
    # Note: One Equal sign (=) is for Assignment, two equal sign (==) is Equality
    # Modulo Operator % = is used to find the remainder of a division operation
        
number = (int(input("What is the number you want to check if odd or even?"))% 2)

if number == 0:
        print ("This number is EVEN!")
else:
        print("This number is ODD!")

# Course Explanation
number = int(input("What is the number you want to check"))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Note: if you add the modulo operator directly to the source, 
#       you won't be able to recall the function later on.

#____________________________________________________________________________________________
# Python Pizza Delivery Challenge
print("Welcome to the Python Pizza Deliveries!")
size = input ("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on you pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N")

pizza_bill = 0
if size == "S":
      pizza_bill = 15
      if pepperoni == "Y":
        pizza_bill  += 2
      if pepperoni == "N":     
        pizza_bill  = 15
      if extra_cheese == "Y":
        pizza_bill  += 1
        print(f"Your pizza total price comes down to ${pizza_bill}")
      if extra_cheese == "N":
        pizza_bill  += 0
        print (f"Your pizza total price is {pizza_bill}")              
if size == "M":
      pizza_bill  = 20
      if pepperoni == "Y":
        pizza_bill  += 3
      if pepperoni == "N":     
        pizza_bill  = 20
      if extra_cheese == "Y":
        pizza_bill  += 1
        print(f"Your pizza total price comes down to ${pizza_bill}")
      if extra_cheese == "N":
        pizza_bill  += 0
        print (f"Your pizza total price is {pizza_bill}")         
if size == "L":     
      pizza_bill  = 25
      if pepperoni == "Y":
        pizza_bill  += 3
      if pepperoni == "N":     
        pizza_bill  = 25
      if extra_cheese == "Y":
        pizza_bill  += 1
        print(f"Your pizza total price comes down to ${pizza_bill}")
      if extra_cheese == "N":
        pizza_bill  += 0
        print (f"Your pizza total price is {pizza_bill}") 

#_______________________________________________________________________________________________
# TREASURE ISLAND!

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/      /_
*******************************************************************************''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure!")
road = input("You are at a crossroad, do you want to go left or right?" "LEFT or RIGHT:").strip().upper()
while road not in ["LEFT","RIGHT"]:
        road = input("Invalid choice. Please choose LEFT or RIGHT: ").strip().upper()
if road == "LEFT":
    print("You were surrounded by wolf pack and killed, GAME OVER")
elif road == "RIGHT":
    print ("You have come acros a river, do you want to swim across or wait for the boat that flowing in your direction?")
    river = input("Swim across, or wait for the boat?" "SWIM or WAIT" ).strip().upper()
    while river not in ["SWIM","WAIT"]:
        river = input("Invalid choice. Please choose SWIM or WAIT: ").strip().upper()
    if river == "SWIM":
        print("You got eaten by sharks, alligators, and piranha, GAME OVER!")
    elif river == "WAIT":
        print("The boat has arrived, and you sailed across the river without any issues!")
        print("You now find yourself inside the dungeon, three door path, red, black, and blue, where do you go?")
        path = input("Which door path will you pick?" "RED, BLACK, or BLUE").strip().upper()
        while path not in ["RED","BLACK","BLUE"]:
            path = input("Invalid choice. Please choose RED, BLACK, or BLUE: ").strip().upper()
        if path == "RED":
            print("You fell into a room of lava, GAME OVER!")
        elif path == "BLACK":
            print ("The room is pitch black, and you get attacked by zombies lying in wait, GAME OVER!")
        elif path == "BLUE":
            print("You have reached the TREASURE, well done! Mission Accomplished!")
    



        


