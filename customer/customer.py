# Import the Review class from the review module
from review import Review

# Define the Customer class
class Customer:
    # Constructor to initialize the customer object with given name and family name
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []  # A list to store reviews left by this customer

    # Method to retrieve the given name of the customer
    def get_given_name(self):
        return self.given_name

    # Method to retrieve the family name of the customer
    def get_family_name(self):
        return self.family_name

    # Method to retrieve the full name of the customer
    def get_full_name(self):
        return f"{self.given_name} {self.family_name}"

    # Method to add a review for a restaurant with a rating
    def add_review(self, restaurant, rating):
        # Create a new Review instance using the Review class
        review = Review(self, restaurant, rating)
        self.reviews.append(review)  # Add the review to the list of reviews for this customer
        restaurant.add_review(review)  # Call the add_review method of the Restaurant class