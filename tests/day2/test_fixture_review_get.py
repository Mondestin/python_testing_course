
# Ce test utilise une fixture définit dans le fichier conftest.py
# Une fixture est un scénario de test réutilisable pour définir des préconditions constantes à des tests.
# Il est automatiquement importé et il suffit de l'ajouter dans les parenthèses du test.
# La variable "returned" par la fixture peut être utilisée directement.
def test_get_with_fixture(restaurant_reviews_with_two_restaurants):

  # Getting a review for "Cafe Mocha" from the fixture
    result = restaurant_reviews_with_two_restaurants.get_review("Cafe Mocha")
    
    # check if the obtained review matches the expected data
    assert result == {'review_text': "Great Coffee.", 'rating': 4}
    
    # Getting a review for "Cafe Burger" from the fixture
    result2 = restaurant_reviews_with_two_restaurants.get_review("Cafe Burger")
    
    # check if the obtained review matches the expected data
    assert result2 == {'review_text': "Good Burger", 'rating': 3}
