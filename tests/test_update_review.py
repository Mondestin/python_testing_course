from restaurant_reviews import RestaurantReviews

# Test to update an existing review for a restaurant
def test_update_existing_review():
    # Creating an instance of the RestaurantReviews class
    rr = RestaurantReviews()
    
    # Adding a review for "Sushi Spot" with a review text and a rating of 4
    rr.add_review("Sushi Spot", "Fresh and tasty sushi.", 4)
    
    # Updating the review for "Sushi Spot" with new review text and a rating of 5
    update_result = rr.update_review("Sushi Spot", "Exceptional sushi and service.", 5)
    
    # Retrieving the updated review for "Sushi Spot"
    get_result = rr.get_review("Sushi Spot")
    
    #check if the review was updated and matches the expected data
    assert update_result == "Review added for Sushi Spot."
    assert get_result == {'review_text': "Exceptional sushi and service.", 'rating': 5}

# Test to update a non-existent review for a restaurant
def test_update_non_existent_review():
    # Creating an instance of the RestaurantReviews class
    rr = RestaurantReviews()
    
    # Attempting to update a review for "Grill House" (which doesn't exist)
    result = rr.update_review("Grill House", "Best steaks in town.", 5)
    
    #check if the attempt to update a non-existent review results in the expected message
    assert result == "Review not found."
