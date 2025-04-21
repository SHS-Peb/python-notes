#   # Lists === Array
# # fruits = ["apple", 'banana', "lemon"]
# #.append() === .push()

# # ------------------------------------------------------
#   #        Prompts
# # Prompt 1: Grocery List
# # Ask the user 3 things to buy from the store
# # Add them to a list
# # Print the final shopping list

# shopping = []

# shopping.append(input("1st thing?"))
# shopping.append(input("2nd thing?"))
# shopping.append(input("3rd thing?"))

# print("Your shopping list has:", shopping)
# # --------------------------
# #  Prompt 2: Count to 10
# # Write a loop that prints numbers 1 to 10 using range()

# for i in range(1, 11):
#   print(i)

# # -----------------
# #  Prompt 3: Playlist Maker
# # Ask the user to name 5 songs they love. Store them in a list. Then:
# #     Print: “Your playlist:”
# #     Print each song on a new line

# playlist = []
# playlist.append(input("1st song you love?"))
# playlist.append(input("2nd song you love?"))
# playlist.append(input("3rd song you love?"))
# playlist.append(input("4th song you love?"))
# playlist.append(input("5th song you love?"))

# for playlist in playlist:
#   print(playlist)


# # Bonus: Random Choice

# # Let the user add items to a list of snacks. When they’re done, randomly pick one snack from the list to “eat”.
# import random
# snacks = []

# def snackQ ():
#   question = input("Would you like to add a snack?")
#   while question == "yes":
#     snacks.append(input("What snack would you add?"))
#     question = input("Would you like to add a snack?")
#   else:
#     print(f"Your random snack is {random.choice(snacks)}")

# snackQ()

# ----------------------------------
# Dictionaries
# ----------------------------------

# Dictionary in Python === Objects in Javascript

# person = {
#   "name": "Shan",
#   "age": 25, # KEYs are the labels & VALUES are the data within
#   "favourite_colour": "Pink"
# }

# print(person["name"])
# [] square brackets to access the VALUE

#  ------------------------------------------------------
#           Prompts
#  Prompt 1: Contact Card
# Ask the user:
#     Their name
#     Their age
#     Their favorite color

# Put the answers in a dictionary.
# Then print the full dictionary AND each value nicely.
# Bonus - Let them update their favorite color if they want!

# person = {
#   "name": "Shan",
#   "age": 25,
#   "favourite_colour": "Pink",
# }

# print(person)
# person["favourite_colour"] = input("What is your new favourite colour?")
# print(person)


# ===========================================
# Prompt 2: Dice Tracker
#     Make a dictionary to count how many times each number (1–6) is rolled
#     Let the user roll the dice up to 10 times (or until they say “stop”)
#     At the end, print how many times each number appeared!

# # Example output:
# # You rolled:
# # 1: 2 times
# # 2: 1 time
# # 3: 0 times
# # ...

import random
diceTracking = { 
  "1": 0,
  "2": 0,
  "3": 0,
  "4": 0,
  "5": 0,
  "6": 0,
}

roll = input("Want to roll the dice?")

while roll == "yes":
  roll = random.randint(1, 6)
  roll = input(f"You rolled {roll} want to roll again?")

print(diceTracking)

#  Prompt 3: Smoothie Bar
#     Create a dictionary of ingredients and prices:
#     Ask the user what 3 ingredients they want.
#     Add up the total price using the dictionary.
#     Print a cute smoothie message with the total cost.

menu = {
  "banana": 1.50,
  "strawberry": 2.00,
  "mango": 2.50,
}

def addMenu ():
  name = input("What is the ingrediants name?")
  price = int(input("And how much?"))
  menu[name] = price

addMenu()
print (menu)
