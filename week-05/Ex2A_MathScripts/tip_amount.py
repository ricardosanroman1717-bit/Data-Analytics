# Restaurant tip calculator with user input

# Ask the user for their bill
bill = float(input("How much was your restaurant bill? "))

# Ask for the tip percentage
tip_percent = float(input("What percentage would you like to tip? "))

# Calculate tip
tip_amount = bill * (tip_percent / 100)

# Display result
print(f"The tip on a ${bill:.2f} restaurant bill is ${tip_amount:.2f}")

# input() returns text, so float() converts it to a number.
# Entering letters instead of numbers causes a ValueError.
# Negative numbers are possible without validation.