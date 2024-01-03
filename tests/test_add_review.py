# Importing the RestaurantReviews class from the restaurant_reviews module
from restaurant_reviews import RestaurantReviews

# Test for adding a valid review
def test_add_valid_review():
    # Creating an instance of the RestaurantReviews class
    rr = RestaurantReviews()

    # Adding a review for "Cafe Mocha" with a review text and a rating of 4
    result = rr.add_review("Cafe Mocha", "Great coffee and pastries.", 4)
    
    #check if the review was added successfully
    assert result == "Review added for Cafe Mocha."
    
    # check if the added review details match the expected data
    assert rr.get_review("Cafe Mocha") == {'review_text': "Great coffee and pastries.", 'rating': 4}

# Test for adding a review with an invalid rating
def test_add_invalid_rating():
    # Creating an instance of the RestaurantReviews class
    rr = RestaurantReviews()
    
    # Attempting to add a review for "Cafe Mocha" with an invalid rating (6)
    result = rr.add_review("Cafe Mocha", "Good ambiance.", 6)
    assert result == "Invalid rating. It must be between 1 and 5."
