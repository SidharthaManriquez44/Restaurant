import os
from datetime import datetime

class BookingManager:
    def __init__(self, file_name):
        self.file_name = file_name
        # We ensure that the file exists
        if not os.path.exists(file_name):
            with open(file_name, 'w'):
                pass

    @staticmethod
    def _format_entry(name, age, reservation_time):
        if isinstance(reservation_time, datetime):
            reservation_time = reservation_time.strftime("%Y-%m-%d %H:%M")
        return f"{name},{age},{reservation_time}\n"

    def add_booking(self, name, age, reservation_time):
        entry = self._format_entry(name, age, reservation_time)

        # Check for line break at the end of the file
        needs_newline = False
        if os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0:
            with open(self.file_name, 'rb') as f:
                f.seek(-1, os.SEEK_END)
                last_char = f.read(1)
                if last_char != b'\n':
                    needs_newline = True

        # Add the reservation
        with open(self.file_name, 'a', encoding='utf-8') as f:
            if needs_newline:
                f.write('\n')
            f.write(entry)

    def read_bookings(self):
        with open(self.file_name, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    name, age, reservation_time = line.strip().split(",", 2)
                    yield {
                        "name": name,
                        "age": int(age),
                        "reservation_time": datetime.strptime(reservation_time, "%Y-%m-%d %H:%M")
                    }
                except ValueError:
                    continue  # Skip badly formatted lines

    def eligible_for_welcome_drink(self):
        return (
            booking for booking in self.read_bookings()
            if booking["age"] >= 21
        )
