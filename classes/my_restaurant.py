from restaurant import Restaurant 

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