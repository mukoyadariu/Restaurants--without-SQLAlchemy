from customer.customer import Customer
from review.review import Review
from restaurant.restaurant import Restaurant


customer1 = Customer("Mike", "joseph")
customer2 = Customer("Gordon", "wummy")

restaurant1 = Restaurant("KFC")
restaurant2 = Restaurant("BURGER KING")
review1 = Review(customer1, restaurant1, 6)
review2 = Review(customer2, restaurant2, 7)

# Use methods
print("Customer name:", customer1.get_full_name())
print("Restaurant name:", restaurant1.get_name())
print("Review rating:", review1.get_rating())

# Adding reviews
customer1.add_review(restaurant1, 5)
customer2.add_review(restaurant2, 4)

# Display restaurant reviews
print("\nRestaurant reviews for", restaurant1.get_name())
for review in restaurant1.get_reviews():
    print("- Rating:", review.get_rating())
    print("  Customer:", review.get_customer().get_full_name())

print("\nRestaurant reviews for", restaurant2.get_name())
for review in restaurant2.get_reviews():
    print("- Rating:", review.get_rating())
    print("  Customer:", review.get_customer().get_full_name())


average_rating1 = restaurant1.average_star_rating()
average_rating2 = restaurant2.average_star_rating()
print("\nAverage rating for", restaurant1.get_name(), ":", average_rating1)
print("Average rating for", restaurant2.get_name(), ":", average_rating2)

