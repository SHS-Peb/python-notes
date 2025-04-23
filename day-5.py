from datetime import datetime

now = datetime.now()
hour = now.hour

if hour < 12:
    greeting = "Good morning!"
elif hour < 18:
    greeting = "Good afternoon!"
else:
    greeting = "Good evening!"

print(greeting)
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))