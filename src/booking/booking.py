import os
from datetime import datetime
from data.config import BOOKINGS_FILE

class BookingManager:
    def __init__(self, file_name=BOOKINGS_FILE):
        self.file_name = file_name
        if not os.path.exists(file_name):
            with open(file_name, 'w'):
                pass

    @staticmethod
    def _format_entry(customer, number_of_tables):
        reservation_time = customer.reservation_time.strftime("%Y-%m-%d %H:%M") if isinstance(customer.reservation_time, datetime) else str(customer.reservation_time)
        return f"{customer.name},{customer.age},{customer.number_of_persons},{reservation_time},{number_of_tables}\n"

    def add_booking(self, customer, number_of_tables):
        entry = self._format_entry(customer, number_of_tables)

        needs_newline = False
        if os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0:
            with open(self.file_name, 'rb') as f:
                f.seek(-1, os.SEEK_END)
                last_char = f.read(1)
                if last_char != b'\n':
                    needs_newline = True

        with open(self.file_name, 'a', encoding='utf-8') as f:
            if needs_newline:
                f.write('\n')
            f.write(entry)

    def read_bookings(self):
        with open(self.file_name, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    name, age, number_of_persons, reservation_time, number_of_tables = line.strip().split(",", 4)
                    yield {
                        "name": name,
                        "age": int(age),
                        "number_of_persons": int(number_of_persons),
                        "reservation_time": datetime.strptime(reservation_time, "%Y-%m-%d %H:%M"),
                        "number_of_tables": int(number_of_tables)
                    }
                except ValueError:
                    continue

    def eligible_for_welcome_drink(self):
        return (
            booking for booking in self.read_bookings()
            if booking["age"] >= 21
        )
