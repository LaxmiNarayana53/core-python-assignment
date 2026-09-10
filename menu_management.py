"""
Restaurant Menu Management
Allows adding, removing, and checking restaurant menu items.
"""

def add_item(menu, item):
    """Add an item to the menu if it does not already exist."""
    if item not in menu:
        menu.append(item)
    else:
        print(f"{item} is already on the menu.")


def remove_item(menu, item):
    """Remove an item from the menu."""
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} is not available on the menu.")


def check_item(menu, item):
    """Check whether an item is available."""
    return f"{item} is available" if item in menu else f"{item} is not available"


def main():
    menu = ["Pizza", "Burger", "Pasta", "Salad"]

    add_item(menu, "Tacos")
    remove_item(menu, "Salad")

    print("Updated menu:", menu)
    print("Availability:", check_item(menu, "Pizza"))


if __name__ == "__main__":
    main()
