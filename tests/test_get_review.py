# Importing the RestaurantReviews class from the restaurant_reviews module
from restaurant_reviews import RestaurantReviews

# Test to retrieve an existing review
def test_get_existing_review():
    # Creating an instance of the RestaurantReviews class
    rr = RestaurantReviews()
    
    # Adding a review for "Pasta Palace" with a review text and a rating of 5
    rr.add_review("Pasta Palace", "Delicious pasta dishes.", 5)
    
    # Retrieving the review for "Pasta Palace"
    result = rr.get_review("Pasta Palace")
    
    #check if the retrieved review matches the expected data
    assert result == {'review_text': "Delicious pasta dishes.", 'rating': 5}

# Test to retrieve a non-existent review
def test_get_non_existent_review():
    # Creating an instance of the RestaurantReviews class
    rr = RestaurantReviews()
    
    # Attempting to retrieve a review for "Burger Bistro" (which doesn't exist)
    result = rr.get_review("Burger Bistro")
    
    # check if the retrieval of a non-existent review results in the expected message
    assert result == "Review not found."
