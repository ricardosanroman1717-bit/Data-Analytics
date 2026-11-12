# Exercise 4.A Lab 2 - Gross Pay Calculator

# Starting values
pay_rate = 17.30
hours_worked = 45

# Calculate gross pay with overtime rules
if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * pay_rate

# Display results
print(f"Gross weekly pay: ${gross_pay:.2f}")