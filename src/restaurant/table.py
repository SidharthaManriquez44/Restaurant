from src.restaurant.customer import Customer

class Table:
    def __init__(self, table_id: int, seats: int = 4):
        self.table_id = table_id
        self.seats = seats
        self.assigned_customers = []
        self.orders = []
        self.is_reserved = False
        self.current_booking = None

    def assign_customer(self, customer: Customer):
        self.assigned_customers.append(customer)
        self.current_booking = customer
        self.is_reserved = True

    def __repr__(self):
        if self.current_booking:
            return f"Booking {self.current_booking.number_of_persons} seats in the table {self.table_id} for {self.current_booking.name}"
        else:
            return f"Table {self.table_id} is available"

