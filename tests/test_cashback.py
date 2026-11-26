import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from cashback import calculate_cashback, calculate_discount


def test_calculate_cashback():
    assert calculate_cashback(100) == 5.0


def test_calculate_discount():
    assert calculate_discount(200.0, 15) == 170.0
