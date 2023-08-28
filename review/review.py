class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.reviews.append(self)

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.reviews
