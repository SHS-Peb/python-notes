#Loops
#        While loops

count = 0

while count < 5:
  print("Counting", count)
  count += 1

#While loops & user input

password = ""

while password != "unicorn":
  password = input("Password?")
  
print("granted access")
#^no white space here is important

#         For loop

for i in range (3):
   print(i, ". This is a loop")

#range() takes a starting value and ending value
#Generating a list between the numbers given including the starting value and excluding the end value.
#If only one value is given the starting value is assumed as 0
#range(0, 1000) === range(1000)

colours = ["blue", "pink", "green"]

for colours in colours:
  print("I see", colours)

#        Functions


def greeting (name):
  print("Hello", name)

greeting("Shan")

def sum (a, b):
  print(a + b)

sum(1, 2)

#        Prompts
# Prompt 1: Password Loop
# Ask the user to enter a password until they get it right.
# Secret password: "seashell"
# When correct, print a friendly message.

 password = ""

 while password != "seashell":
  password = input("Do you know the password?")

 print ('correct! Come in please!') 

  # Prompt 2: Dice Roller
# Make a function called roll_dice() that:
# Picks a random number between 1–6
# Prints the result
# Ask the user: "Roll again? (yes/no)"
# Repeat until they say no.

def roll_dice():
  import random
  roll = random.randint(1, 6)
  print("You rolled", roll, "want to roll again?")

roll_dice()

  #Prompt 3: Compliment Machine
# Make a function called compliment(name)
# It should print something nice about the person whose name is passed in.
# Ask for their name, call the function, and ask if they want another one.
# Keep complimenting until they say "no".

name = ''

def compliment(name):
  print("you have a pretty name")
  again = input("another?")
  while again != "no":
    print("I like your dress")
    again = input("another?")

compliment("shan")

import random 

def compliment(name):
  sayings = [f"I like your hair {name}", 
             f"I like your eyes {name}",
             f"I like your face {name}",]
  print (random.choice(sayings))

name = input("Name please")
again = "yes"

while again != "no":
  compliment(name)
  again = input("Would you like another?").lower()
