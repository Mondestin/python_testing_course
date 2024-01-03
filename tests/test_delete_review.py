import pytest
from restaurant_reviews import RestaurantReviews

# Test to delete an existing review and verify it's deleted
def test_delete_existing():
    # Creating an instance of the RestaurantReviews class
    rr = RestaurantReviews()
    
    # Adding a review for "Sushi Shop" with review text and a rating of 5
    rr.add_review("Sushi Shop", "Delicious pasta dishes.", 5)
    # Deleting the review for "Sushi Shop"
    result = rr.delete_review("Sushi Shop")
    # check if the review was deleted successfully
    assert result == "Review deleted for Sushi Shop"
   
    # Retrieving the review for "Sushi Shop" to ensure it's not found
    result2 = rr.get_review("Sushi Shop") 
    assert(result2 == "Review not found.")

# Test to attempt deleting a non-existing review
def test_delete_non_existing():
    # Creating an instance of the RestaurantReviews class
    rr = RestaurantReviews()
    #delete a review for a restaurant that doesn't exist
    with pytest.raises(ValueError) as e:
        rr.delete_review('Unknown Restaurant')
    
    #check if the attempt to delete a non-existing review raises the expected ValueError
    assert str(e.value) == "Review not found to delete."
