class Restaurant:
    instances = []  # Class variable to track all restaurant instances

    # Constructor to initialize a restaurant with a given name
    def __init__(self, name):
        self.name = name
        self.reviews = []  # List to store reviews left for this restaurant
        Restaurant.instances.append(self)  # Add the restaurant instance to the instances list

    # Method to retrieve the name of the restaurant
    def get_name(self):
        return self.name

    # Method to add a review to the restaurant's reviews list
    def add_review(self, review):
        self.reviews.append(review)  # Add the review to the restaurant's reviews list

    # Method to retrieve the list of reviews for this restaurant
    def get_reviews(self):
        return self.reviews

    # Method to retrieve the set of customers who left reviews for this restaurant
    def get_customers(self):
        customers = set()
        for review in self.reviews:
            customers.add(review.get_customer())
        return customers

    # Method to calculate the average star rating for this restaurant
    def average_star_rating(self):
        total_ratings = sum(review.get_rating() for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return 0.0