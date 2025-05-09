class TableManager:
    def __init__(self, tables, booking_manager=None):
        self.tables = tables
        self.booking_manager = booking_manager

    def find_available_tables(self, customer):
        required = customer.number_of_persons
        available_tables = [t for t in self.tables if not t.is_reserved]
        selected_tables = []

        for table in sorted(available_tables, key=lambda t: t.seats):  # mesas pequeñas primero
            if required <= 0:
                break
            selected_tables.append(table)
            required -= table.seats

        if required > 0:
            raise ValueError("There are not enough tables available for this reservation.")

        # Assign tables
        for table in selected_tables:
            table.assign_customer(customer)

        # Register reservation
        if self.booking_manager:
            self.booking_manager.add_booking(customer, number_of_tables=len(selected_tables))

        return selected_tables
