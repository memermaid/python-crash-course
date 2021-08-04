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
    
restaurant1 = Restaurant('Olive Garden', 'american')
restaurant2 = Restaurant('Bahama Breeze', 'caribbean')
restaurant3 = Restaurant('Grazie Restorante', 'italian')

restaurant1.set_number_served(10)
restaurant1.increment_number_served(5)
restaurant1.describe_restaurant()
print(f"{restaurant1.restaurant_name} served {restaurant1.number_served} customers today.")

restaurant2.set_number_served(5)
restaurant2.increment_number_served(7)
restaurant2.describe_restaurant()
print(f"{restaurant2.restaurant_name} served {restaurant2.number_served} customers today.")

restaurant3.set_number_served(8)
restaurant3.increment_number_served(13)
restaurant3.describe_restaurant()
print(f"{restaurant3.restaurant_name} served {restaurant3.number_served} customers today.")


