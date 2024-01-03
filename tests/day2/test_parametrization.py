import pytest

# Function to calculate price including VAT
def vta_price(ht, vta):
    return round(ht * (1 + vta / 100), 2)

# Test cases using @pytest.mark.parametrize to test various VAT rates for French prices
@pytest.mark.parametrize("prix, taux, prix_ttc_attendu", [
    # Test cases for different VAT rates in France
    (100, 20, 120),     # Normal rate
    (100, 10, 110),     # Intermediate rate (rounded to two decimals due to floating point issues)
    (100, 5.5, 105.5),  # Reduced rate
    (100, 2.1, 102.1),  # Special rate
    (100, 0, 100),      # Zero rate
    # Add test cases for other countries like Luxembourg...
])
def test_french_vta(prix, taux, prix_ttc_attendu):
    # Calculate the total price including VAT
    ttc = vta_price(prix, taux)
    
    #check if the calculated total matches the expected total after applying VAT
    assert ttc == prix_ttc_attendu
