# Exercise 4.C Lab 4 - Sales Performance

# Employee sales records
sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25)
]

# Start total sales at zero
total_sales = 0

# Loop through employee records
for name, region, sales in sales_data:

    print(f"{name} ({region}): ${sales:,.2f}")

    # Identify top performers
    if sales > 5000:
        print(" ^ Top performer!")

    # Add each employee's sales to the total
    total_sales += sales

# Display total company sales
print(f"Total company sales: ${total_sales:,.2f}")