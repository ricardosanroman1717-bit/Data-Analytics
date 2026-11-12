# Exercise 4.B Lab 2 - Greetings

# Current hour (0-23)
hour = 14

# Determine the greeting
if hour < 10:
    print("Good morning!")
elif hour < 17:
    print("Good day!")
else:
    print("Good evening!")

# Check for late-night hours
if hour >= 23 or hour <= 4:
    print("What are you doing up so late??")