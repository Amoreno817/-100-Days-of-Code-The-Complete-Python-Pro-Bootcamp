import random
from game_data import data

print('''
██   ██ ██  ██████  ██   ██ ███████ ██████      ██       ██████  ██     ██ ███████ ██████  
██   ██ ██ ██       ██   ██ ██      ██   ██     ██      ██    ██ ██     ██ ██      ██   ██ 
███████ ██ ██   ███ ███████ █████   ██████      ██      ██    ██ ██  █  ██ █████   ██████  
██   ██ ██ ██    ██ ██   ██ ██      ██   ██     ██      ██    ██ ██ ███ ██ ██      ██   ██ 
██   ██ ██  ██████  ██   ██ ███████ ██   ██     ███████  ██████   ███ ███  ███████ ██   ██ 
                                                                                           
''')

print("Welcome to the Higher Lower Game!")

score = 0

def play_game():
    global score
    while True:
        # Choose two random entries
        random_entry_a = random.choice(data)
        random_entry_b = random.choice(data)

        # Ensure they are not the same
        while random_entry_b == random_entry_a:
            random_entry_b = random.choice(data)

        # Extract follower counts
        choice_a_value = random_entry_a["follower_count"]
        choice_b_value = random_entry_b["follower_count"]

        # Print the options
        print(f"A: {random_entry_a['name']}, {random_entry_a['description']} from {random_entry_a['country']}")
        print("VS")
        print(f"B: {random_entry_b['name']}, {random_entry_b['description']} from {random_entry_b['country']}")
        print("Who do you think is more popular?")
        
        # Get player input
        player_choice = input("Choose A or B: ").strip().upper()

        # Compare follower counts
        if (player_choice == "A" and choice_a_value > choice_b_value) or (player_choice == "B" and choice_b_value > choice_a_value):
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break  # Exit the loop when the guess is wrong

# Start the game
play_game()

# Points to Validate:
# Global score: The use of global for score ensures that the player's score persists across
# the game loop. This part is correctly implemented.

# Infinite Loop Safeguard: The while True loop with the break statement properly exits the 
# game when the player guesses incorrectly. This avoids unnecessary recursion.
