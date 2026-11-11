# Exercise 3.A Lab 2 - String Cleaning

# Original messy data
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# Convert names to lowercase
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# Convert names to title case
print(name_1.title())
print(name_2.title())
print(name_3.title())

# Remove dollar signs
clean_salary_1 = salary_1.replace("$", "")
clean_salary_2 = salary_2.replace("$", "")

print(clean_salary_1)
print(clean_salary_2)

# Check the data types
print(type(clean_salary_1))
print(type(clean_salary_2))

# Remove symbols and convert to integer
usable_salary = int(salary_1.replace("$", "").replace(",", ""))

print(usable_salary)
print(type(usable_salary))

# Removing dollar signs still leaves text.
# I must also remove commas and convert the
# value to int() before doing calculations.