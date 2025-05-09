class Customer:
    def __init__(self, name, age=None, number_of_persons=1, reservation_time=None):
        self.name = name
        self.age = age
        self.number_of_persons = number_of_persons
        self.reservation_time = reservation_time

    def __repr__(self):
        return f"Customer is registered {self.name} at {self.reservation_time}"
