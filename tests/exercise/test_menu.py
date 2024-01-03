import pytest
from menu import Menu

@pytest.fixture
def menu_instance():
    return Menu()

def test_add_menu_item(menu_instance):
    # Testing adding a menu item and retrieving the menu for a restaurant
    assert menu_instance.add_menu_item("Restaurant A", "Burger", "Tasty Burger", 9.99) == "Menu item 'Burger' added for 'Restaurant A'."
    assert menu_instance.get_menu("Restaurant A") == [{'item_name': 'Burger', 'description': 'Tasty Burger', 'price': 9.99}]

def test_update_menu_item(menu_instance):
    # Testing updating a menu item and verifying the updated details
    menu_instance.add_menu_item("Restaurant B", "Pizza", "Delicious Pizza", 12.99)
    assert menu_instance.update_menu_item("Restaurant B", "Pizza", "Amazing Pizza", 15.99) == "Menu item 'Pizza' updated for 'Restaurant B'."
    assert menu_instance.get_menu("Restaurant B") == [{'item_name': 'Pizza', 'description': 'Amazing Pizza', 'price': 15.99}]

def test_delete_menu_item(menu_instance):
    # Testing deleting a menu item and verifying the menu for the restaurant is empty
    menu_instance.add_menu_item("Restaurant C", "Salad", "Healthy Salad", 7.99)
    assert menu_instance.delete_menu_item("Restaurant C", "Salad") == "Menu item 'Salad' deleted for 'Restaurant C'."
    assert menu_instance.get_menu("Restaurant C") == []

def test_get_menu_for_non_existent_restaurant(menu_instance):
    # Testing retrieving menu for a non-existent restaurant
    assert menu_instance.get_menu("NonExistentRestaurant") == []

def test_update_non_existent_item(menu_instance):
    # Testing updating a non-existent menu item
    assert menu_instance.update_menu_item("Restaurant D", "NonExistentItem", "New Description", 10.99) == "Menu item 'NonExistentItem' not found for 'Restaurant D'."
