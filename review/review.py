# Define the Review class
class Review:
    # Constructor to initialize a review with a customer, restaurant, and rating
    def __init__(self, customer, restaurant, rating):
        self.customer = customer  # The customer who left the review
        self.restaurant = restaurant  # The restaurant that was reviewed
        self.rating = rating  # The rating given to the restaurant

    # Method to retrieve the rating of the review
    def get_rating(self):
        return self.rating

    # Method to retrieve the customer who left the review
    def get_customer(self):
        return self.customer

    # Method to retrieve the restaurant that was reviewed
    def get_restaurant(self):
        return self.restaurant