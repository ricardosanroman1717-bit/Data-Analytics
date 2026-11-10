# Rule of 72 savings calculator

# Starting values
savings = 500
interest_rate = 0.06

# Calculate doubled savings
doubled_savings = savings * 2

# Calculate years needed to double
years = 72 / (interest_rate * 100)

# Display results
print(f"Your current savings is {savings}.")
print(f"At a {interest_rate:.0%} interest rate, your savings account will be worth {doubled_savings:.2f} in {years:.1f} years")