# Dictionaries and Nesting
# Format = Dictionary {"keys":"values",}
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function":"A piece of code that you can easily call over and over again",
                          "Loop":"The action of doing something over and over again."}
list[programming_dictionary]

print (programming_dictionary["Bug"])
programming_dictionary ["Loop"] = "The action of doing something over and over again."

empty_dictionary={}
empty_dictionary

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)

#________________________________________________________________________________________________________________________
# Grading Program
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
 
# Create an empty dictionary to collect the new values.
student_grades = {}
 
# Loop through each key in the student_scores dictionary
for student in student_scores:
 
    #Get the value (student score) by using the key each time.
    score = student_scores[student]
 
    #Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

#____________________________________________________________________________________________________________________________
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary, Creating a key with miltiple values!
travel_log = {
"France": ["Paris", "Lille", "Dijan"],
"Germany":["Stuggart" , "Berlin"]
}

print(travel_log["France"][1])
# Call out "D", which is a list within a list, listception
nested_list = ["A", "B", ["C" , "D"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

print(travel_log["Germany"]["cities_visited"][2])

#________________________________________________________________________________________________________________________________
# The Secret Auction 

# The Secret Auction 

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________
                         `'-------'`
                       .-------------.
                      /_______________\     
''')
print("Welcome to the Secret Auction!")

# Initialize an empty registry for bidders
registry = {}

# Main auction loop
while True:
    name = input("What is your name?: ")
    
    # Handle bid input and validate it's a positive integer
    while True:
        try:
            bid = int(input("What is your bid price?: $"))
            if bid <= 0:
                raise ValueError("Bid must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid bid.")

    registry[name] = bid  # Add the bidder's name and bid to the registry
    
    # Ask if there are more bidders
    add = input("Are there any other users that would like to bid? (YES/NO): ").strip().upper()
    while add not in {"YES", "NO"}:
        add = input("Invalid answer. Please type 'YES' or 'NO': ").strip().upper()
    
    if add == "NO":
        break  # Exit the loop if no more bidders

# Clear the screen for final output
print("\n" * 100)

# Find the highest bidder
if registry:
    highest_bidder = max(registry, key=registry.get)
    print("Thank you for all the bidding. Bidding is now closed.")
    print(f"The winner is {highest_bidder} with a bid of ${registry[highest_bidder]}!")
else:
    print("No bids were placed.")

# Square Brackets []: Access or define elements in lists or dictionaries.
# Curly Brackets {}: Create dictionaries or sets.
# Parentheses (): Group operations, call functions, or define tuples.
