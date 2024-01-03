import pytest
from restaurant_reviews import RestaurantReviews

# Test to remove valid reviews for different restaurants
@pytest.mark.parametrize("restaurant_title, review_text, review_rating, expected_output", [
    # Test cases for removing valid reviews from different restaurants
    ("Cafe Mocha", "Great coffee and pastries.", 4, "Review deleted for Cafe Mocha"),
    ("Cafe Bürger", "Great coffee and Bürger.", 2, "Review deleted for Cafe Bürger"),
    ("Cafe Pizza", "Great coffee and Pizza.", 3, "Review deleted for Cafe Pizza"),
    ("Cafe Sushi", "Great coffee and Sushi.", 5, "Review deleted for Cafe Sushi"),
    ("Cafe Tacos", "Great coffee and Tacos.", 1, "Review deleted for Cafe Tacos"),
])


def test_remove_valid_review(restaurant_title, review_text, review_rating, expected_output):
    # Creating an instance of RestaurantReviews
    rr = RestaurantReviews()
    
    # Adding a review for a restaurant
    rr.add_review(restaurant_title, review_text, review_rating)
    
    # Removing the review for the restaurant
    result = rr.delete_review(restaurant_title)
    
    # check if the review was deleted and matches the expected output
    assert result == expected_output
    
    # Verifying that the review for the restaurant is not found after deletion
    result2 = rr.get_review(restaurant_title) 
    assert result2 == "Review not found."

# Test to handle attempting to delete reviews for non-existing restaurants
@pytest.mark.parametrize("non_existing_restaurant, expected_output", [
    # Test cases for attempting to delete reviews for non-existing restaurants
    ("Cafe Mocha", "Review not found to delete."),
    ("Cafe Bürger", "Review not found to delete."),
    ("Cafe Pizza", "Review not found to delete."),
    ("Cafe Sushi", "Review not found to delete."),
    ("Cafe Tacos", "Review not found to delete."),
])


def test_delete_non_existing(non_existing_restaurant, expected_output):
    # Creating an instance of RestaurantReviews
    rr = RestaurantReviews()
    
    # Attempting to delete a review for a non-existing restaurant and expecting a ValueError
    with pytest.raises(ValueError) as e:
        rr.delete_review(non_existing_restaurant)
    
    # check if the raised ValueError message matches the expected output
    assert str(e.value) == expected_output
