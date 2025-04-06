import datetime

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menus = {}  # dict {id_menu: Menu}

    def add_menu(self, menu):
        self.menus[menu.id_menu] = menu

    def available_menus(self, time=None):
        if time is None:
            time = datetime.datetime.now().time()
        available = []

        for menu in self.menus.values():
            start = datetime.datetime.strptime(menu.start_time, "%H:%M").time()
            end = datetime.datetime.strptime(menu.end_time, "%H:%M").time()
            if start <= time <= end:
                available.append(menu)

        if available:
            result = "Menus available now:\n"
            for menu in available:
                result += f"\n🧾 {menu.name} ({menu.start_time} - {menu.end_time}):\n"
                result += menu.show_items()
                result += "\n" + "-"*30 + "\n"
            return result
        else:
            return "Sorry, we are closed.\n"
