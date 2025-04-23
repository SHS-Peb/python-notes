from datetime import datetime
now = datetime.now()

print("Today's date is:", now.date())
print("The time is:", now.strftime("%H:%M:%S"))