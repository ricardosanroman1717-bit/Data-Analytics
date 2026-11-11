# Calculate charter van rentals

import math

# Starting values
tourists = 38
van_capacity = 15
cost_per_van = 250

# Calculate vans needed
vans_needed = math.ceil(tourists / van_capacity)

# Calculate rental cost
total_cost = vans_needed * cost_per_van

# Calculate cost per person, rounding up to cents
cost_per_person = math.ceil((total_cost / tourists) * 100) / 100

# Calculate total collected
collected = cost_per_person * tourists

# Calculate leftover money
leftover = collected - total_cost

# Display results
print(f"Vans needed: {vans_needed}")
print(f"Total rental cost: ${total_cost:.2f}")
print(f"Charge per person: ${cost_per_person:.2f}")
print(f"Money collected: ${collected:.2f}")
print(f"Leftover money: ${leftover:.2f}")
# There is leftover money because the cost per
# person was rounded up to the nearest cent.