from datetime import datetime

now = datetime.now()
hour = now.hour

if hour < 12:
    greeting = "Morning Barbie!!"
elif hour < 18:
    greeting = "Afternoon Bestie!"
else:
    greeting = "Good Evening Girly!!"

print(greeting)
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))