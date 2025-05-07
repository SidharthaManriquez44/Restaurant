from data.config import RESTAURANT_NAME, LIST_FILE
from data.menu_data import get_default_menus
from datetime import datetime
from src.restaurant.restaurant import Restaurant
from src.booking.booking import BookingManager

def show_menus(restaurant):
    print("\n📋 Menús registrados:")
    for menu in restaurant.menus.values():
        print(menu)
        print(menu.show_items())
        print("-" * 40)

def make_booking():
    manager = BookingManager(LIST_FILE)

    print("\n🔖 Crear nueva reserva:")
    name = input("Nombre del cliente: ")
    age = int(input("Edad del cliente: "))
    date_input = input("Fecha y hora de reserva (formato: YYYY-MM-DD HH:MM): ")

    try:
        reservation_time = datetime.strptime(date_input, "%Y-%m-%d %H:%M")
        manager.add_booking(name, age, reservation_time)
        print("✅ Reserva registrada con éxito.")
    except ValueError:
        print("❌ Formato de fecha inválido. Intenta con: 2025-05-07 18:00")

    print("\n📒 Reservas registradas:")
    for booking in manager.read_bookings():
        print(booking)

    print("\n🍸 Bienvenida con cóctel:")
    for guest in manager.eligible_for_welcome_drink():
        print(f"{guest['name']} ({guest['age']} años)")


def run_cli():
    restaurant = Restaurant(RESTAURANT_NAME)
    menus = get_default_menus()
    for menu in menus.values():
        restaurant.add_menu(menu)

    while True:
        print("Bienvenido al sistema de Restaurante")
        print("1. Ver menú")
        print("2. Hacer reserva")
        print("3. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            show_menus(restaurant)
        elif choice == "2":
            make_booking()
        elif choice == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")
