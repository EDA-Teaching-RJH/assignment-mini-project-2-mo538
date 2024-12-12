import pytest
from health_checker import calculate_percentage, health_status # import from health checker.py

def test_calculate_percentage():
    # Test percentage calculations
    assert calculate_percentage(2000, 10000) == 20
    assert calculate_percentage(6500, 10000) == 65
    assert calculate_percentage(10000, 10000) == 100
    assert calculate_percentage(25000, 10000) == 250

def test_calculate_percentage_zero_division():
    # Test division by zero
    with pytest.raises(ZeroDivisionError):
        calculate_percentage(5000, 0)

def test_health_status():
    # Test feedback message based on percentages
    assert health_status(30, "Steps") == "You're falling behind on your Steps goal. Keep going you can do this :)!"
    assert health_status(50, "Water") == "You're on track with your Water goal. Keep it up!"
    assert health_status(90, "Steps") == "You're doing well on your Steps goal. Welldone!"
    assert health_status(110, "Water") == "Good job! You've exceeded your Water goal!"
