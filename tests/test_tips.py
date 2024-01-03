import pytest

# Exception definition for negative values
class NegativeValueError(Exception):
    """Custom exception for handling negative values in bill and percentage"""
    pass
    
# Function that calculates the total bill with tip
def total_with_tip(bill, percentage):
    # Customizing exception messages for negative values
    if bill < 0:
        raise NegativeValueError("Bill should be positive")
    if percentage < 0:
        raise NegativeValueError("Percentage should be positive")
    
    # Calculating the tip with an upper limit of 500
    tip = bill * percentage / 100
    if tip > 500:
        tip = 500
    
    # Ensuring the total is at least 5
    total = bill + tip
    if total < 5:
        total = 5
    return round(total, 2)

# Test cases for the total_with_tip function

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

# Test 5: Handling exceptions for negative bill and percentage values.
def test_negative_error():
    with pytest.raises(NegativeValueError) as exceptionTips:
        total_with_tip(100, -10)
    assert str(exceptionTips.value) == "Percentage should be positive"

    with pytest.raises(NegativeValueError) as exceptionBill:
        total_with_tip(-10, 10)
    assert str(exceptionBill.value) == "Bill should be positive"
