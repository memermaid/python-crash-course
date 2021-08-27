class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, customers_number):
        self.number_served = customers_number

    def increment_number_served(self, customers_number):
        self.number_served += customers_number