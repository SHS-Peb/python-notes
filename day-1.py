# Hello World & variables
print("Hello World")

age = 25
name = "Shannon"
colour = "Blue"

print("My name is", name, "I am", age, "and my favourite colour is", colour)

# Changing variables
colour = "Pink"
print("Now my favourite colour is", colour)


#Type conversion
age = input("How old are you?")
name = input("What is your name?")
colour = input("What is your favourite colour?")

print ("My name is", name, "I am", age, "and my favourite colour is", colour, ".")

#input will always be treated as a string

age = int(input("How old are you?"))
print(age)

countCars = int(input("How many red cars?"))
print(countCars)

#String Methods
name = "shan"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(len(name))


# Prompt 1
# What year were they born?
# What year it is now? Then print how old they are.

yearBorn = int(input("What year were you born?"))
currentYear = 2025

age = currentYear - yearBorn

print("You are", age, "years old.")

# Prompt 2: Mini Math Game
# Ask the user: A number and another number
# Then print the:
# Sum
# Difference
# Product
# Result of division

num1 = int(input("Please give me a random number"))
num2 = int(input("And how about another please?"))

print("The sum is", num1 + num2)
print("The difference is", num1 - num2)
print("The product is", num1 * num2)
print("The result of division is", num1 / num2)
#use // for full number or just / for float


# Prompt 3: Name Styling
# Ask the user for their name, then:
# Print it all uppercase
# All lowercase
# The number of letters in their name

name = input("May I have your name please?")

print("Your name in uppercase is", name.upper())
print("Your name in lowercase is", name.lower())
print("Your name capitalised is", name.capitalize())
print(f"Your name is {len(name)} characters long")

# 🌈 Prompt 1: Mood Checker
# Ask the user:
# “How are you feeling today?”
# If they type:
# "happy" → print something uplifting
# "sad" → print something comforting
# "angry" → print something grounding
# anything else → print a neutral encouragement

mood = input("How are you feeling today?")

if mood == "happy":
  print ("I'm so glad!")
elif mood == "sad":
  print ("aw want a hug?")
elif mood == "angry":
  print("smell the flower, blow out the candle")
else:
  print(f"Tell me about it, today is so {mood}")

# Prompt 2: Age Gate
# Ask the user for their age.
# If they're under 13: "You're too young for this app."
# 13–17: "Come back when you're 18!"
# 18+: "Welcome in!"

age = int(input("what age are you?"))

if age < 13:
  print("You are too young for this app!")
elif age >= 18:
  print("Welcome in!")
else: 
  print("Come back when you are 18!")


# Prompt 3: Secret Word Game
# Ask the user:
# "What's the secret word?"
# If they guess "pineapple", print "Correct! 🍍"
# If they guess "apple", print "Close, but not tropical enough."
# Anything else → "Nope! Try again later."

guess = input("What's the secret word?")

if guess == "apple":
  print("Close but not tropical enough!")
elif guess == "pineapple":
  print("Correct!")
else: 
  print("Nope! Try again!")
