"""
Taxi Fare Calculation
Calculates fares for multiple trips.

Base fare = $50
Distance fare = $10 per kilometer
"""

BASE_FARE = 50
DISTANCE_RATE = 10


def calculate_fare(distance):
    """Calculate the fare for one trip."""
    if distance < 0:
        raise ValueError("Distance cannot be negative.")

    return BASE_FARE + (distance * DISTANCE_RATE)


def calculate_total_fare(trips):
    """Calculate the total fare for all trips."""
    return sum(calculate_fare(distance) for distance in trips)


def main():
    trips = [5, 10, 3]

    for number, distance in enumerate(trips, start=1):
        fare = calculate_fare(distance)
        print(f"Trip {number}: ${fare:.0f}")

    total_fare = calculate_total_fare(trips)
    print(f"Total Fare: ${total_fare:.0f}")


if __name__ == "__main__":
    main()
