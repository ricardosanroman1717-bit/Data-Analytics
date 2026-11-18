class Restaurant:
    """Store a restaurant's name and food type and display its information."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


restaurant1 = Restaurant("Sunset Tacos", "Mexican food")
restaurant2 = Restaurant("Pasta House", "Italian food")
restaurant3 = Restaurant("Sakura Sushi", "Japanese food")

restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()
