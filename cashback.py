"""Simple cashback and discount calculations for the quality gate lab."""

CASHBACK_RATE = 0.05


def calculate_cashback(price: float) -> float:
    """Return 5% cashback for a purchase, rounded to two decimal places."""
    return round(price * CASHBACK_RATE, 2)


def calculate_discount(price: float, discount_percent: int) -> float:
    return round(price * (1 - discount_percent / 100), 2)
