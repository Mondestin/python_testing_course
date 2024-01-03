import pytest
from restaurant_reviews import RestaurantReviews

# Fixture to create a RestaurantReviews instance with two added restaurants for scenarios
@pytest.fixture
def restaurant_reviews_with_two_restaurants():
    # Creating an instance of RestaurantReviews
    rr = RestaurantReviews()
    
    # Adding two restaurants with reviews for test scenarios
    rr.add_review("Cafe Mocha", "Great Coffee.", 4)
    rr.add_review("Cafe Burger", "Good Burger", 3)
    
    # Returning the RestaurantReviews instance with the added restaurants
    return rr
