  # Lists === Array
# fruits = ["apple", 'banana', "lemon"]
#.append() === .push()

# ------------------------------------------------------
  #        Prompts
# Prompt 1: Grocery List
# Ask the user 3 things to buy from the store
# Add them to a list
# Print the final shopping list

shopping = []

shopping.append(input("1st thing?"))
shopping.append(input("2nd thing?"))
shopping.append(input("3rd thing?"))

print("Your shopping list has:", shopping)
# --------------------------
#  Prompt 2: Count to 10
# Write a loop that prints numbers 1 to 10 using range()

for i in range(1, 11):
  print(i)

# -----------------
#  Prompt 3: Playlist Maker
# Ask the user to name 5 songs they love. Store them in a list. Then:
#     Print: “Your playlist:”
#     Print each song on a new line

playlist = []
playlist.append(input("1st song you love?"))
playlist.append(input("2nd song you love?"))
playlist.append(input("3rd song you love?"))
playlist.append(input("4th song you love?"))
playlist.append(input("5th song you love?"))

for playlist in playlist:
  print(playlist)


# Bonus: Random Choice

# Let the user add items to a list of snacks. When they’re done, randomly pick one snack from the list to “eat”.
import random
snacks = []

def snackQ ():
  question = input("Would you like to add a snack?")
  while question == "yes":
    snacks.append(input("What snack would you add?"))
    question = input("Would you like to add a snack?")
  else:
    print(f"Your random snack is {random.choice(snacks)}")

snackQ()
