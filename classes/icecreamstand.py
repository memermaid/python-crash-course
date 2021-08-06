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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def show_flavors(self):
        print(f"{self.restaurant_name} offers the following flavors:")
        for flavor in self.flavors:
            print("-", flavor)
            

baskin_robins = IceCreamStand("Baskin Robins", "ice cream")
baskin_robins.flavors = ['chocolate', 'vanilla', 'strawberry']
baskin_robins.show_flavors()