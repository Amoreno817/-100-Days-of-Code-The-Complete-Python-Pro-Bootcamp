# For & While Loops, IF/ELSE, List, Strings, Range, Modules

# Step 1: Word List, ask the user, check if guess answer is correct

import random

word_list = ["python","hangman", "challenge","programming","developer","keyboard","monitor",
"internet","variable","function","loop","algorithm","condition","boolean","debugging","syntax",
"exception","inheritance","polymorphism","recursion","iteration","dictionary","tuple","module",
"package","argument","parameter","framework","library","dynamic","static","compile","runtime",
"binary","hexadecimal","database","server","frontend","backend","cloud","software","hardware",
"encryption","security","networking","machine","learning","artificial","intelligence","debugger"]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chosen_word = random.choice(word_list) # AI chooses a random word from the word list.
word_length = len(chosen_word) # Measure the length of the random chosen word.
display = ["_" for _ in range(word_length)]  # Create blanks for the word.
guessed_letters = [] # used to keep track of all the letters the player has guessed so far
lives = 6  # Number of incorrect guesses allowed
print(''' 
___                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                __/ |                      
                |___/                    ''')
print(" ".join(display))
print("Greetings Player! Welcome to the hangman game!\n Get ready to pick a letter!")
# Loop, Display, isalpha()

# Main game loop VERY IMPORTANT TO KEEP THE GAME GOING
while "_" in display and lives > 0:
    # Ask for player's guess
    player_choice = input("Guess a letter: ").strip().lower()

 # Validating Input   
    if not player_choice.isalpha() or len(player_choice) != 1:
        print("Invalid choice, please choose a letter!") 
        continue

    if player_choice in guessed_letters:
        print(f"You already guessed {player_choice}, please select another letter!")
        continue

    # Add the guess to guessed_letters
    guessed_letters.append(player_choice)
     
    #Check if the letters guess is in the word 
     
    if player_choice in chosen_word:
        print("You guessed right! Pick another letter!")
        # Update display with correct guesses
        for index,letters in enumerate(chosen_word):
            if letters == player_choice:
                display [index] = player_choice

    #Incorrect guess
    else:
        lives -= 1
        print(f"Wrong guess! You now have {lives} remaining.")

    # Show the current state of the word
    print(" ".join(display))

# The End
if "_" not in display:
    print(f"Congratulation, you guessed the word! The word was {chosen_word}!")
else:
    print(f"GAME OVER! You lost all your lives. The word was {chosen_word}!")
    




