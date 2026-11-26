from cashback import calculate_cashback, calculate_discount


def test_calculate_cashback():
    assert calculate_cashback(200.0) == 10.0


def test_calculate_discount():
    assert calculate_discount(200.0, 15) == 170.0
