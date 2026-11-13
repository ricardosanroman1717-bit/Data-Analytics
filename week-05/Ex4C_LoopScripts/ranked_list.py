# Exercise 4.C Lab 3 - Ranked List

# Create a list of favorite foods
favorite_foods = [
    "Tacos",
    "Ramen",
    "Pizza",
    "Jerk Chicken",
    "Burgers"
]

# Display the ranked list
for position, food in enumerate(favorite_foods, start=1):

    print(f"{position}. {food}", end="")

    if position == 1:
        print(" <- top pick!")
    else:
        print()