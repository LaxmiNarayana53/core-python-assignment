"""
Movie Ticket Booking System
Manages available and booked cinema seats.
"""

def book_seat(booked_seats, seat_number, total_seats):
    """Book a seat if it is valid and available."""
    if seat_number < 1 or seat_number > total_seats:
        print("Invalid seat number.")
        return

    if seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked.")
        return

    booked_seats.append(seat_number)
    print(f"Seat {seat_number} booked successfully.")


def cancel_seat(booked_seats, seat_number):
    """Cancel a previously booked seat."""
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        print(f"Seat {seat_number} cancelled successfully.")
    else:
        print(f"Seat {seat_number} is not booked.")


def get_available_seats(total_seats, booked_seats):
    """Return a list of available seats."""
    return [
        seat for seat in range(1, total_seats + 1)
        if seat not in booked_seats
    ]


def main():
    total_seats = 10
    booked_seats = [2, 5, 7]

    book_seat(booked_seats, 3, total_seats)
    cancel_seat(booked_seats, 5)

    available_seats = get_available_seats(total_seats, booked_seats)
    print("Available seats:", available_seats)


if __name__ == "__main__":
    main()
