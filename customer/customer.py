class Customer:
    customers = []

    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name
        self.customers.append(self)

    def given_name(self):
        return self.name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.customers
