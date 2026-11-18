import pytest
from booking import booking_total
def test_quantity_nine():
    with pytest.raises(ValueError):
        booking_total("test@example.com", 9, 10)
def test_quantity_zero():
    with pytest.raises(ValueError):
        booking_total("test@example.com", 0, 10)
def test_negative_price():
    with pytest.raises(ValueError):
        booking_total("test@example.com", 2, -10)
def test_valid_booking():
    assert booking_total("test@example.com", 2, 10) == 20
