#  Blackjack rules: You draw a car, the dealer draws a card. If you draw a card that is higher than the dealer's card, you win. 
#  If both cards are the same, it's a draw. If the dealer's card is higher, you lose.
#  However, if you draw a card that is higher than 21, you lose.  

import random

print('''
88888888ba  88                       88        88                       88         
88      "8b 88                       88        ""                       88         .------.------.------.------.
88      ,8P 88                       88                                 88         |A_  _ |A /\  |A _   |A .   |
88aaaaaa8P' 88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   |( \/ )| /  \ | ( )  | / \  |
88""""""8b, 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    | \  / | \  / |(_x_) |(_,_) |
88      `8b 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      |  \/ A|  \/ A|  Y  A|  I  A|
88      a8P 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   `------^------^------'------' 
88888888P"  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"
''')

print("Welcome to the Blackjack game!")

# Card values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []

# Function to deal a card
def deal_card():
    return random.choice(cards)

# Function to calculate the score
def calculate_score(card_list):
    # Handle the Ace (11 or 1)
    if sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

# Main game function
def play_blackjack():
    # Initial deal (2 cards for each)
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    
    print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    # Check for blackjack or bust immediately
    if calculate_score(player_cards) == 21:
        return "Blackjack! You win!"
    if calculate_score(dealer_cards) == 21:
        return "Dealer has Blackjack! You lose!"

    # Player's turn
    while calculate_score(player_cards) < 21:
        should_continue = input("Do you want to draw another card? Type 'y' for yes or 'n' for no: ").lower()
        if should_continue == 'y':
            player_cards.append(deal_card())
            print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
        else:
            break

    # Check if player busts
    if calculate_score(player_cards) > 21:
        return "You went over 21. You lose!"

    # Dealer's turn
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())

    print(f"Dealer's cards: {dealer_cards}, final score: {calculate_score(dealer_cards)}")

    # Compare scores
    if calculate_score(dealer_cards) > 21:
        return "Dealer went over 21. You win!"
    elif calculate_score(player_cards) > calculate_score(dealer_cards):
        return "You win!"
    elif calculate_score(player_cards) < calculate_score(dealer_cards):
        return "You lose!"
    else:
        return "It's a draw!"

# Start the game
print(play_blackjack())