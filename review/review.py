class Review:
    instances = []  # Class variable to track all review instances

    # Constructor to initialize a review with a customer, restaurant, and rating
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.instances.append(self)  # Add the review instance to the instances list

    # Method to retrieve the rating of the review
    def get_rating(self):
        return self.rating

    # Method to retrieve the customer who left the review
    def get_customer(self):
        return self.customer

    # Method to retrieve the restaurant that was reviewed
    def get_restaurant(self):
        return self.restaurant