class Restaurant:
    """Store restaurant information, customer counts, and customer ratings."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        while True:
            answer = input("How many customers served today? ")
            try:
                number = int(answer)
                if number < 0:
                    print("Please enter a nonnegative whole number.")
                    continue
            except ValueError:
                print("Please enter a nonnegative whole number.")
                continue
            self.number_served += number
            break

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    def customer_rating(self):
        while True:
            answer = input("How would you rate your experience today on a scale of 1-5 (5 being excellent)? ")
            try:
                rating = int(answer)
            except ValueError:
                print("Please enter a whole number from 1 to 5.")
                continue
            if not 1 <= rating <= 5:
                print("Please enter a whole number from 1 to 5.")
                continue
            self.customer_ratings.append(rating)
            average = sum(self.customer_ratings) / len(self.customer_ratings)
            print(f"Your rating was {rating}. The average rating for this restaurant is {average:.2f}")
            break


restaurant1 = Restaurant("Sunset Tacos", "Mexican food")
restaurant2 = Restaurant("Pasta House", "Italian food")
restaurant3 = Restaurant("Sakura Sushi", "Japanese food")

for restaurant in (restaurant1, restaurant2, restaurant3):
    print(f"\n{restaurant.rest_name}")
    restaurant.describe_rest()
    restaurant.rest_open()
    restaurant.print_num_served()
    for _ in range(2):
        restaurant.add_num_served()
    restaurant.print_num_served()
    for _ in range(3):
        restaurant.customer_rating()
