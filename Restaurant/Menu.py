class Menu:
    def __init__(self, id_menu, name, start_time, end_time, items):
        self.id_menu = id_menu
        self.name = name
        self.start_time = start_time  # Expected format: 'HH:MM'
        self.end_time = end_time
        self.items = items  # Dict: {item_name: price}

    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

    def show_items(self):
        if not self.items:
            return "  (No items available)"
        return '\n'.join([f"  - {item.title()}: ${price:.2f}" for item, price in self.items.items()])
