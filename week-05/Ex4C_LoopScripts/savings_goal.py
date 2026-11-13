# Exercise 4.C Lab 2 - Savings Goal

# Starting values
bank_balance = 100
savings_goal = 500
weekly_savings = 50
treat_cost = 5

# Repeat until the savings goal is reached
while bank_balance < savings_goal:

    bank_balance += weekly_savings

    print(f"This week my balance increased to ${bank_balance:.2f}.")

    # Check if we've reached 75% of the goal
    if bank_balance >= savings_goal * 0.75 and bank_balance < savings_goal:
        bank_balance -= treat_cost
        print(f"So close! After treating myself, my balance is up to ${bank_balance:.2f}.")

    # Check if we're more than halfway there
    elif bank_balance > savings_goal * 0.50 and bank_balance < savings_goal:
        print(f"Almost there! This week my balance is up to ${bank_balance:.2f}.")

# Display the final balance
print(f"Goal met! My current balance is ${bank_balance:.2f}.")