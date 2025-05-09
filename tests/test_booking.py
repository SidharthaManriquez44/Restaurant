from src.booking.booking import BookingManager
from src.restaurant.customer import Customer
from datetime import datetime
import pytest


@pytest.fixture
def temp_booking_file(tmp_path):
    file = tmp_path / "bookings_test.txt"
    return str(file)

def test_add_read_booking(temp_booking_file):
    manager = BookingManager(temp_booking_file)

    customer1 = Customer("Sofía Salas", 25, 3, datetime(2025, 5, 10, 18, 30))
    customer2 = Customer("John Smith", 49, 4, datetime(2025, 5, 10, 20, 0))

    manager.add_booking(customer1, 1)
    manager.add_booking(customer2, 2)

    bookings = list(manager.read_bookings())

    assert len(bookings) == 2
    assert bookings[0]["name"] == "Sofía Salas"
    assert bookings[1]["age"] == 49
    assert bookings[1]["reservation_time"] == datetime(2025, 5, 10, 20, 0)
    assert bookings[1]["number_of_tables"] == 2

def test_eligible_for_welcome_drink(temp_booking_file):
    manager = BookingManager(temp_booking_file)

    c1 = Customer("Mario Perez", 49, 2, datetime(2025, 5, 11, 19, 0))
    c2 = Customer("Javier Granados", 40, 3, datetime(2025, 5, 11, 21, 0))
    c3 = Customer("Raul Duran", 15, 1, datetime(2025, 5, 11, 20, 0))

    manager.add_booking(c1, 1)
    manager.add_booking(c2, 1)
    manager.add_booking(c3, 1)

    eligible = list(manager.eligible_for_welcome_drink())

    assert len(eligible) == 2
    assert all(guest["age"] >= 21 for guest in eligible)

    names = [g["name"] for g in eligible]
    assert "Mario Perez" in names
    assert "Javier Granados" in names
    assert "Raul Duran" not in names
