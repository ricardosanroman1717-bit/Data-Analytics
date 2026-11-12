# Exercise 4.B Lab 3 - Complex Taxes

# Starting values
pay_rate = 20.00
hours_worked = 40
filing_status = "joint"

# Calculate weekly gross pay
if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    weekly_gross = regular_pay + overtime_pay
else:
    weekly_gross = hours_worked * pay_rate

# Estimate annual gross pay
annual_gross = weekly_gross * 52

# Determine tax rate for single filers
if filing_status == "single":
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

# Determine tax rate for joint filers
elif filing_status == "joint":
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.05
    elif annual_gross < 75000:
        tax_rate = 0.10
    else:
        tax_rate = 0.20

else:
    raise ValueError("Filing status must be single or joint")

# Calculate weekly withholding
weekly_tax = weekly_gross * tax_rate

# Calculate net pay
net_pay = weekly_gross - weekly_tax

# Display results
print(f"You worked {hours_worked} hours this period.")
print(f"Your hourly rate is ${pay_rate:.2f}")
print(f"Your gross weekly pay is ${weekly_gross:.2f}")
print(f"Your estimated annual gross pay is ${annual_gross:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax rate is {tax_rate:.0%}")
print(f"Your weekly tax withholding is ${weekly_tax:.2f}")
print(f"Your net weekly pay is ${net_pay:.2f}")