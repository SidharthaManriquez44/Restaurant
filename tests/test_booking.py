import pytest
from datetime import datetime
from src.booking.booking import BookingManager

@pytest.fixture
def temp_booking_file(tmp_path):
    """Create a temporary booking file for testing."""
    file = tmp_path / "reservas_test.txt"
    return str(file)

def test_add_read_booking(temp_booking_file):
    manager = BookingManager(temp_booking_file)

    # Add two Bookings
    manager.add_booking("Sofía Salas", 25,  datetime(2025, 5, 10, 18, 30))
    manager.add_booking("John Smith", 49, datetime(2025, 5, 10, 20, 0))

    bookings = list(manager.read_bookings())

    assert len(bookings) == 2
    assert bookings[0]["name"] == "Sofía Salas"
    assert bookings[1]["age"] == 49
    assert bookings[1]["reservation_time"] == datetime(2025, 5, 10, 20, 0)

def test_eligible_for_welcome_drink(temp_booking_file):
    manager = BookingManager(temp_booking_file)

    # Add bookings with different ages
    manager.add_booking("Mario Perez", 49, datetime(2025, 5, 11, 19, 0))
    manager.add_booking("Javier Granados", 40, datetime(2025, 5, 11, 21, 0))
    manager.add_booking("Raul Duran", 15, datetime(2025, 5, 11, 20, 0))

    eligible = list(manager.eligible_for_welcome_drink())

    assert len(eligible) == 2
    assert all(guest["age"] >= 21 for guest in eligible)
    guest_names = [guest["name"] for guest in eligible]
    assert "Mario Perez" in guest_names
    assert "Javier Granados" in guest_names
    assert "Raul Duran" not in guest_names

