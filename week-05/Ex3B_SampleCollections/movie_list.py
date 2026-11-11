# Exercise 3.B - Movie List

# Create a list of favorite movies
movies = [
    "Interstellar",
    "The Matrix",
    "Inception",
    "Avatar",
    "Gladiator"
]

# Display the list and its length
print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)

# Display a sorted copy
print(sorted(movies))

# Display the original list again
print(movies)

# Sort the original list
movies.sort()
print(movies)

# Add another favorite movie
movies.append("The Dark Knight")

# Display the updated list
print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)
# sorted() displays a sorted copy without changing the original list.
# sort() changes the order of the original list.