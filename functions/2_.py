from curses.ascii import isdigit, islower


def is_strong_pasword(password: str) -> bool:
    """This function checks if a password is strong or not"""

    if len(password) < 8:
        print("Password should be atleast 8 characters")
        return False

    if not any(islower(char) for char in password):
        print("Password should have atleast one Capital letter")
        return False

    return True


def calculate_total_cost(cart_items: list[dict]) -> float:

    sum = 0

    for item in cart_items:
        sum += item["price"] * item["quantity"]

    return sum


is_strong_pasword("ddfdd")

total_cost = calculate_total_cost(
    [
        {"name": "Apple", "price": 20, "quantity": 2},
        {"name": "Chips", "price": 10, "quantity": 4},
    ]
)

print(total_cost)
