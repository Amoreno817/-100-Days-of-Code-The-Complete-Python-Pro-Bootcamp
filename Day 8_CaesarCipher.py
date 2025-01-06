# Standard Fuction
def greet():
    print("Good Morning rookie!\nHope you are ready to work!\nNo days off!")
    print("Create a function called greet, and print three statement!")
    print("Good job, mission accomplished!")

greet()

# Function with Inputs
name = input("What is your name?")


def greet_with_name(name):
    print(f"Good Morning rookie {name}!")
    print(f"No days off {name}!")
    print(f"Get to work {name}!")

greet_with_name(name)

# Parameters = the name of the data that's being passed in
# Arguments = the actual value of the data

current_age = int(input("What is your age?"))

def life_in_weeks(current_age):
    week_left_years = 90 - current_age 
    age_in_weeks = week_left_years * 52
    print(f"You have {age_in_weeks} weeks left.")
    
life_in_weeks(current_age)

# Functions with more than 1 input

name = input ("What is your name?")
location = input("Where do you live?")

def greet_with_name(name, location):
    print(f"Hello, {name}!")
    print(f"How is the weather in {location}?")

greet_with_name(name, location)

# Code Challenge

def calculate_love_score():
    # Get names from the user
    name1 = input("Enter the first name: ").lower()
    name2 = input("Enter the second name: ").lower()
    
    # Combine both names into one string
    combined_names = name1 + name2
    
    # Calculate the count for "TRUE"
    true_count = combined_names.count('t') + combined_names.count('r') + \
                 combined_names.count('u') + combined_names.count('e')
    
    # Calculate the count for "LOVE"
    love_count = combined_names.count('l') + combined_names.count('o') + \
                 combined_names.count('v') + combined_names.count('e')
    
    # Combine the counts to make the love score
    love_score = int(str(true_count) + str(love_count))
    
    # Print the results
    print(f"T occurs {combined_names.count('t')} times")
    print(f"R occurs {combined_names.count('r')} times")
    print(f"U occurs {combined_names.count('u')} times")
    print(f"E occurs {combined_names.count('e')} times")
    print(f"Total TRUE count = {true_count}")
    
    print(f"L occurs {combined_names.count('l')} times")
    print(f"O occurs {combined_names.count('o')} times")
    print(f"V occurs {combined_names.count('v')} times")
    print(f"E occurs {combined_names.count('e')} times")
    print(f"Total LOVE count = {love_count}")
    
    print(f"Love Score = {love_score}")
#__________________________________________________________________________________________________________________________________________
# Caesar Cipher Challenge
print('''                                                                                                             
    //   ) )                                                  //   ) )                                       
   //         ___      ___      ___      ___      __         //        ( )  ___     / __      ___      __    
  //        //   ) ) //___) ) ((   ) ) //   ) ) //  ) )     //        / / //   ) ) //   ) ) //___) ) //  ) ) 
 //        //   / / //         \ \    //   / / //          //        / / //___/ / //   / / //       //       
((____/ / ((___( ( ((____   //   ) ) ((___( ( //          ((____/ / / / //       //   / / ((____   //   ''')
print("Welcome to the Caesar Cipher Challenge!")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']    
# 1: Create a function encrypt() that takes original text and shift amount as 2 inputs.
direction = input("Type 'encode' to encrpyt, type 'decode' to decrypt:\n").lower().strip()
while direction not in ["encode","decode"]:
        direction = input("Invalid choice. Please type 'encode' or 'decode': ").strip().lower()  
text = input("What is the secret phrase you'll like to encrypt?\n")  
shift = int(input("By how many shift would you like to shift the letters?\n"))

if direction == "encode":
    def encrypt(text, shift):
        cipher_text = ""
        for letter in text:
            if letter in alphabet:
                shifted_position = (alphabet.index(letter) + shift) % len(alphabet)
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text += letter  # Keep other characters unchanged

        print(f"Here is the encoded results:{cipher_text}")

# Decryption function
def decrypt(text, shift):
    plain_text = ""
    for letter in text:
        if letter in alphabet:  # Only shift letters in the alphabet
            shifted_position = (alphabet.index(letter) - shift) % len(alphabet)
            plain_text += alphabet[shifted_position]
        else:
            plain_text += letter  # Keep other characters unchanged
    print(f"Here is the decoded result: {plain_text}")

# Call the appropriate function
if direction == "encode":
    encrypt(text, shift)  # Call the encrypt function
elif direction == "decode":
    decrypt(text, shift)  # Call the decrypt function
