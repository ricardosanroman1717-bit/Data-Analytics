# Exercise 3.B Lab 2 - Candy Store

# Create two tuples
candies = ("Gummies", "Lollipops", "Jelly Beans")
flavors = ("Strawberry", "Mango", "Blueberry")

# Create a set of candy combinations
candy_options = {
    candies[0] + " - " + flavors[1],
    candies[1] + " - " + flavors[0],
    candies[2] + " - " + flavors[2]
}

# Display available candy options
print("Today's candy options include:")
print(candy_options)

# Print again to observe the order
print(candy_options)
print(candy_options)

# Sets contain unique values and do not guarantee order.