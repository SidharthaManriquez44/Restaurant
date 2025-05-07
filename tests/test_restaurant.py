import unittest
from src.restaurant.menu import Menu
from src.restaurant.restaurant import Restaurant
from datetime import datetime

class TestRestaurantAndMenu(unittest.TestCase):

    def setUp(self):
        self.menu = Menu(1, "Brunch", "11:00", "16:00", {"pancakes": 7.50, "coffee": 1.50})
        self.kids_menu = Menu(4, "Kids", "11:00", "21:00", {"chicken nuggets": 6.50})

        self.restaurant = Restaurant("Inn Polar")
        self.restaurant.add_menu(self.menu)
        self.restaurant.add_menu(self.kids_menu)

    def test_menu_creation(self):
        self.assertEqual(self.menu.name, "Brunch")
        self.assertIn("pancakes", self.menu.items)
        self.assertAlmostEqual(self.menu.items["pancakes"], 7.50)

    def test_add_menu_to_restaurant(self):
        self.assertEqual(len(self.restaurant.menus), 2)
        self.assertEqual(self.restaurant.menus[1].name, "Brunch")
        self.assertEqual(self.restaurant.menus[4].name, "Kids")

    def test_show_items_format(self):
        result = self.menu.show_items()
        self.assertIn("Pancakes: $7.50", result)
        self.assertIn("Coffee: $1.50", result)

    def test_available_menus_formatted_output(self):
        from datetime import datetime

        # Hora en la que Brunch y Kids están disponibles (Brunch: 11:00–16:00, Kids: 11:00–21:00)
        test_time = datetime.strptime("12:00", "%H:%M").time()
        output = self.restaurant.available_menus(test_time)

        self.assertIn("Menus available now:", output)
        self.assertIn("Brunch (11:00 - 16:00):", output)
        self.assertIn("Kids (11:00 - 21:00):", output)
        self.assertIn("pancakes: $7.50".lower(), output.lower())
        self.assertIn("chicken nuggets: $6.50".lower(), output.lower())

    def test_show_items_content(self):
        time = datetime.strptime("12:00", "%H:%M").time()
        available_menus = self.restaurant.get_available_menus(time)

        brunch_menu = next((menu for menu in available_menus if menu.name == "Brunch"), None)
        self.assertIsNotNone(brunch_menu, "The 'Brunch' menu should be available at 12:00")

        expected_output = (
            " - Pancakes: $7.50\n"
            " - Coffee: $1.50"
        )

        actual_output = brunch_menu.show_items()
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
