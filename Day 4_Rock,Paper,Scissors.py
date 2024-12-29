# Randomization and Python Lists 

import random


random_interger = random.randint(1, 99)
print(random_interger)

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_float = random.uniform (1, 10)
print(random_float)

# Create heads or tails coin flip

heads_or_tails = random.choice(["heads", "tails"])
print(heads_or_tails)

# List = [0,1,2,3,4] or [-5,-4,-3,-2,-1]

fruits = ["Orange" , "Apple", " Strawberry"]
random_fruit = random.choice(fruits)
print(random_fruit)
print(fruits[-2])

fruits.append("AVOCADO")
print(fruits)
fruits.extend("raspberry")
print(fruits)

# Russian Roulete: Who's paying the restaurant bill?
print("Greeting, the DB warriors are eating at an expensive restaurant,\nfind out who is paying the restaurant bill on this episode!")
friends = ["Goku", "Vegeta" , "Chichi" , "Bulma", "Krillin" , "Android 18"]
Who_is_paying = random.choice(friends)
print(f"You are paying the bill this time, {Who_is_paying}!")  

# Nested List

Six_fruits = ["Strawberry","Apple", "Grapes", "Cherry","Peaches", "Pearls"]
Six_vegetables = ["Spinach", "Kale", "Tomatoes","Cherry","Potatoes", "Celery"]

dirty_dozen = [Six_fruits, Six_vegetables]
print(dirty_dozen[1][2])

#________________________________________________________________________________________________
# Project ROCK PAPER SCISSORS!

rock = '''
      ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       
       ROCK'''
paper = '''         
            ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'    
          
        PAPER'''
scissor = '''
     ."".    ."",
     |  |   /  /
     |  |  /  /
     |  | /  /
     |  |/  ;-._
     }  ` _/  / ;
     |  /` ) /  /
     | /  /_/\_/\
     |/  /      |
     (  ' \ '-  |
      \    `.  /
       |      |
       |      |
       
       SCISSOR'''

choices = ["ROCK", "PAPER", "SCISSOR"]
print("Welcome to the rock, paper, scissor game!\nTry your luck and beat the computer on a game of rock, paper, and scissors.\nGOOD LUCK!")
player_choice = input("Pick your move: (ROCK, PAPER, SCISSOR)").strip().upper() 
while player_choice not in ["ROCK", "PAPER", "SCISSOR"]:
    player_choice = input("Invalid choice, please pick ROCK, PAPER, or SCISSOR")

computer_choice = random.choice (choices)

print(f"You choose {player_choice}")
print(f"The computer choose {computer_choice}")

if player_choice == "ROCK" and computer_choice == "PAPER":
    print(rock, paper)
    print("You lost this round, GAME OVER!")
elif player_choice == "SCISSOR" and computer_choice == "PAPER":
    print(scissor, paper)
    print ("You have won, CONGRAT!")
elif player_choice == "PAPER" and computer_choice == "PAPER":
    print(paper, paper)
    print ("It's a draw! Please try again!")

if player_choice == "ROCK" and computer_choice == "ROCK":
    print(rock, rock)
    print ("It's a draw! Please try again!")
elif player_choice == "SCISSOR" and computer_choice == "ROCK":
    print(scissor, rock)
    print("You lost this round, GAME OVER!")
elif player_choice == "PAPER" and computer_choice == "ROCK":
    print(paper, rock)
    print ("You have won, CONGRAT!")

if player_choice == "ROCK" and computer_choice == "SCISSOR":
    print(rock, scissor)
    print ("You have won, CONGRAT!")
elif player_choice == "SCISSOR" and computer_choice == "SCISSOR":
    print(scissor, scissor)
    print ("It's a draw! Please try again!")
elif player_choice == "PAPER" and computer_choice == "SCISSOR":
    print(paper, scissor)
    print("You lost this round, GAME OVER!")

























