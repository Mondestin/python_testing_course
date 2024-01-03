import pytest

# Functions to test

def total_with_tip(bill, percentage):
    # Handling invalid input cases
    if bill < 0:
        raise ValueError("Bill cannot be negative")
    if percentage > 100:
        raise ValueError("Percentage cannot be greater than 100%")
    if percentage < 0:
        raise ValueError("Percentage cannot be negative")
    
    # Calculating tip with upper limit of 500
    tip = bill * percentage / 100
    if tip > 500:
        tip = 500
    
    # Calculating total with lower limit of 5
    total = bill + tip
    if total < 5:
        total = 5
    return round(total, 2)

# Test cases

# Test 1: For a bill of 100€ and a 20% tip, the expected output should be 120€.
def test_tip_classic():
    assert total_with_tip(100, 20) == 120

# Test 2: Testing maximum tip amount (500€ limit).
def test_tip_max():
    assert total_with_tip(1000, 51) == 1500
    assert total_with_tip(5000, 15) == 5500
    assert total_with_tip(2000, 26) == 2500
    assert total_with_tip(10000, 12) == 10500

# Test 3: Ensuring the minimum total is 5€ due to the smallest available bill.
def test_min_total():
    assert total_with_tip(1, 0) == 5
    assert total_with_tip(2.30, 20) == 5
    assert total_with_tip(4, 15) == 5
    assert total_with_tip(3, 50) == 5

# Test 4: Verifying that the total is rounded to two decimal places.
def test_two_decimals():
    assert total_with_tip(5, 12.45) == 5.62
    assert total_with_tip(10.12, 15) == 11.64
    assert total_with_tip(10, 2.33) == 10.23

# Test 5: Handling error cases for invalid percentages and bills.
def test_error_percentage():
    with pytest.raises(ValueError):
        total_with_tip(100, 101)
    with pytest.raises(ValueError):
        total_with_tip(100, -1)

def test_error_bill():
    with pytest.raises(ValueError):
        total_with_tip(-100, 20)
    with pytest.raises(ValueError):
        total_with_tip(-100, 0)
