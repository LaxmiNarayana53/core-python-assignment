"""
E-Commerce Cart System
Calculates the total price of items in a shopping cart.
A 10% discount is applied if there are more than 5 items.
"""

def calculate_total_price(cart_items):
    """Calculate the total price of items in the cart."""
    if not cart_items:
        return 0

    total = sum(cart_items.values())

    if len(cart_items) > 5:
        total *= 0.90

    return total


def main():
    cart_items = {
        "Laptop": 50000,
        "Headphones": 2000,
        "Mouse": 500,
        "Keyboard": 1500
    }

    total_price = calculate_total_price(cart_items)
    print(f"Total Price: {total_price:.2f}")


if __name__ == "__main__":
    main()
