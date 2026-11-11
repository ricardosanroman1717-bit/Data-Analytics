# Description: This script tests various numeric
#              conversion techniques
# Author: Ricardo Sanroman

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Check original values and data types
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
# Test converting variable a

# a_integer = int(a)  # ValueError: Cannot convert decimal text directly to int

a_float = float(a)
print(a_float, type(a_float))

a_integer = int(float(a))
print(a_integer, type(a_integer))
# Test converting variable b

b_integer = int(b)
print(b_integer, type(b_integer))

b_float = float(b)
print(b_float, type(b_float))
# Test converting variable c

# c_integer = int(c)  # ValueError: Contains letters
# Extract the numeric portion using slicing
c_slice = c[:3]

print(c_slice, type(c_slice))

# Convert the extracted text into an integer
c_number = int(c_slice)

print(c_number, type(c_number))
# Test converting variable d

# d_integer = int(d)  # ValueError: Contains letters
# d_float = float(d)  # ValueError: Contains letters

# Extract the number using slicing
d_slice = d[7:8]

print(d_slice, type(d_slice))

# Convert extracted text into an integer
d_number = int(d_slice)

print(d_number, type(d_number))
# Test removing extra spaces

print(a.strip())
print(d.strip())

# strip() removes spaces from the beginning
# and end of a string, but not the middle.
# Additional slicing practice

a_slice = a[1:6]
print(a_slice, type(a_slice))

b_slice = b[:2]
print(b_slice, type(b_slice))