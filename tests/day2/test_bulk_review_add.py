import pytest
from restaurant_reviews import RestaurantReviews

# Test to add valid reviews using parameterized values for different restaurants
@pytest.mark.parametrize("restaurant_title, review_text, review_rating, expected_output", [
    # Test cases for adding valid reviews to different restaurants
    ("Cafe Mocha", "Great coffee and pastries.", 4, "Review added for Cafe Mocha."),
    ("Cafe Bürger", "Great coffee and Bürger.", 2, "Review added for Cafe Bürger."),
    ("Cafe Pizza", "Great coffee and Pizza.", 3, "Review added for Cafe Pizza."),
    ("Cafe Sushi", "Great coffee and Sushi.", 5, "Review added for Cafe Sushi."),
    ("Cafe Tacos", "Great coffee and Tacos.", 1, "Review added for Cafe Tacos."),
])
def test_add_valid_review(restaurant_title, review_text, review_rating, expected_output):
    # Creating an instance of RestaurantReviews
    rr = RestaurantReviews()
    
    # Adding a review for a restaurant with specific review text and rating
    result = rr.add_review(restaurant_title, review_text, review_rating)
    
    # Assertion to check if the result matches the expected output after adding the review
    assert result == expected_output
