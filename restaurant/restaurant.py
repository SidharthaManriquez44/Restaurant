from datetime import datetime

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menus = {}  # dict {id_menu: Menu}

    def add_menu(self, menu):
        self.menus[menu.id_menu] = menu

    def get_available_menus(self, current_time=None):

        if current_time is None:
            current_time = datetime.now().time()

        available = []

        for menu in self.menus.values():
            start = datetime.strptime(menu.start_time, "%H:%M").time()
            end = datetime.strptime(menu.end_time, "%H:%M").time()
            if start <= current_time <= end:
                available.append(menu)

        return available

    def available_menus(self, current_time=None):
        available = self.get_available_menus(current_time)

        if available:
            result = "Menus available now:\n"
            for menu in available:
                result += f"\n{menu.name} ({menu.start_time} - {menu.end_time}):\n"
                result += menu.show_items()
                result += "\n" + "-" * 30 + "\n"
            return result.strip()
        else:
            return "Sorry, we are closed."
