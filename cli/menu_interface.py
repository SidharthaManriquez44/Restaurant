from data.config import RESTAURANT_NAME, BOOKINGS_FILE
from data.menu_data import get_default_menus
from datetime import datetime
from src.restaurant.restaurant import Restaurant
from src.restaurant.customer import  Customer
from src.restaurant.table import  Table
from src.booking.booking import BookingManager
from src.restaurant.table_manager import TableManager

def show_menus(restaurant):
    print("\n📋 Registered menus:")
    for menu in restaurant.menus.values():
        print(menu)
        print(menu.show_items())
        print("-" * 40)

def make_booking(table_manager):
    print("\n🔖 Create new booking:")
    name = input("Customer name ")
    age = int(input("Client age: "))
    persons = int(input("Number of people: "))
    date_input = input("Reservation date and time (formato: YYYY-MM-DD HH:MM): ")

    try:
        reservation_time = datetime.strptime(date_input, "%Y-%m-%d %H:%M")
    except ValueError:
        print("❌ Invalid date format. Try: 2025-05-07 18:00")
        return

    customer = Customer(name, age, persons, reservation_time)

    try:
        tables = table_manager.find_available_tables(customer)
        print(f"✅ Registered reservation. They were assigned {len(tables)} table(s).")
    except ValueError as e:
        print(f"❌ {str(e)}")
        return

    print("\n📒 Registered reservations:")
    for booking in table_manager.booking_manager.read_bookings():
        print(booking)

    print("\n🍸 Welcome cocktail")
    for guest in table_manager.booking_manager.eligible_for_welcome_drink():
        print(f"{guest['name']} ({guest['age']} years)")

def run_cli():
    restaurant = Restaurant(RESTAURANT_NAME)
    menus = get_default_menus()
    for menu in menus.values():
        restaurant.add_menu(menu)

    # Suppose we have fixed tables, for now 3 tables with 2, 4 and 6 seats
    tables = [Table(1, 2), Table(2, 4), Table(3, 6)]
    booking_manager = BookingManager(BOOKINGS_FILE)
    table_manager = TableManager(tables, booking_manager)

    while True:
        print("\nWelcome to the Restaurant system")
        print("1. See menu")
        print("2. Make Booking")
        print("3. Close")

        choice = input("Select an option: ")

        if choice == "1":
            show_menus(restaurant)
        elif choice == "2":
            make_booking(table_manager)
        elif choice == "3":
            print("See you later!")
            break
        else:
            print("Invalid option")
