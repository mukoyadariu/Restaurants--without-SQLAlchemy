# Import the Review class from the review module
from review.review import Review

# Define the Customer class
class Customer:
    # Class variable to track all customer instances
    instances = []

    # Constructor to initialize a customer with given name and family name
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []  # List to store reviews left by this customer
        Customer.instances.append(self)  # Add the customer instance to the instances list

    # Method to retrieve the given name of the customer
    def get_given_name(self):
        return self.given_name

    # Method to retrieve the family name of the customer
    def get_family_name(self):
        return self.family_name

    # Method to retrieve the full name of the customer
    def get_full_name(self):
        return f"{self.given_name} {self.family_name}"

    # Class method to retrieve all customer instances
    @classmethod
    def all(cls):
        return cls.instances

    # Method to add a review for a restaurant with a rating
    def add_review(self, restaurant, rating):
        # Create a new Review instance using the Review class
        review = Review(self, restaurant, rating)
        self.reviews.append(review)  # Add the review to the list of reviews for this customer
        restaurant.add_review(review)  # Call the add_review method of the Restaurant class

    # Method to get the number of reviews left by this customer
    def num_reviews(self):
        return len(self.reviews)

    # Class method to find a customer by their full name
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.instances:
            if customer.get_full_name() == name:
                return customer
        return None

    # Class method to find all customers with a given given_name
    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.instances if customer.get_given_name() == given_name]
