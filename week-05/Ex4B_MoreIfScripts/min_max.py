# Exercise 4.B Lab 4 - Find Smallest and Largest

a = 25
b = 10
c = 40

# Find the smallest number
if a < b:
    smallest = a
else:
    smallest = b

if c < smallest:
    smallest = c

# Find the largest number
if a > b:
    largest = a
else:
    largest = b

if c > largest:
    largest = c

# Display results
print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")