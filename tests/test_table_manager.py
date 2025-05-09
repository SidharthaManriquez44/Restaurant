from src.restaurant.customer import Customer
from datetime import datetime
from src.restaurant.table import Table
from src.booking.booking import BookingManager
from src.restaurant.table_manager import TableManager
import pytest

@pytest.fixture
def temp_booking_file(tmp_path):
    file = tmp_path / "bookings_test.txt"
    return str(file)

def test_find_available_tables(temp_booking_file):
    customer_salas = Customer("Sara Salas", 41, 2, datetime(2025, 5, 10, 18, 30))
    customer_pacheco = Customer("Celia Pacheco", 49, 8, datetime(2025, 5, 10, 20, 0))
    table_north = Table(1, 2)
    table_south = Table(2, 8)

    bm = BookingManager(temp_booking_file)
    manager = TableManager([table_north], bm)
    mg = TableManager([table_south], bm)

    assignations =  list(manager.find_available_tables(customer_salas))
    assignations_2 = list(mg.find_available_tables(customer_pacheco))

    assert assignations[0].table_id == 1
    assert assignations_2[0].table_id == 2
    assert assignations[0].seats == 2
    assert assignations_2[0].seats == 8




