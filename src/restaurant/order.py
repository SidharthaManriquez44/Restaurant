from datetime import datetime
from src.restaurant.table import Table

class Order:
    _order_counter = 1  # Counter to assign unique IDs

    def __init__(self, table: Table, items: dict, timestamp: datetime = None):
        self.order_id = Order._order_counter
        Order._order_counter += 1
        self.table = table
        self.items = items  # Dictionary: {item_name: quantity}
        self.timestamp = timestamp or datetime.now()


    def calculate_total(self, menu):
        total = 0
        for item_name, quantity in self.items.items():
            if item_name in menu.items:
                total += menu.items[item_name] * quantity
            else:
                raise ValueError(f"The ítem '{item_name}' it's not on the menu.")
        return total

    def __repr__(self):
        return f"Order {self.order_id} for the table {self.table.table_id}."
