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
def name_bid():
    name = input("What is your name?")
    bid = input("What is your bud price?")
    registry = {name,bid}
add = input("Are there any other user that would like to bid?").strip().upper()
while add not in {"YES","NO"}.strip().upper():
    add = input("Invalid answer, please choose YES or NO")

while add == "yes":
    name_bid()
else: