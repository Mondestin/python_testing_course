class Menu:
    def __init__(self):
        # Initializes a dictionary to store menus for each restaurant
        self.menus = {}

    def add_menu_item(self, restaurant_name, item_name, description, price):
        # Adds a new menu item to a specific restaurant's menu
        if restaurant_name not in self.menus:
            # If the restaurant doesn't exist in the menus dictionary, create an empty list for its menu
            self.menus[restaurant_name] = []
        
        # Appends the new item details (name, description, price) to the restaurant's menu list
        self.menus[restaurant_name].append({
            'item_name': item_name,
            'description': description,
            'price': price
        })
        
        # Returns a confirmation message indicating the successful addition of the item
        return f"Menu item '{item_name}' added for '{restaurant_name}'."

    def get_menu(self, restaurant_name):
        # Retrieves the menu for a given restaurant name
        # If the restaurant doesn't exist, returns an empty list
        return self.menus.get(restaurant_name, [])

    def update_menu_item(self, restaurant_name, item_name, new_description, new_price):
        # Updates the description and price of an existing menu item in a restaurant's menu
        if restaurant_name in self.menus:
            for item in self.menus[restaurant_name]:
                if item['item_name'] == item_name:
                    # Finds the matching item by name and updates its description and price
                    item['description'] = new_description
                    item['price'] = new_price
                    return f"Menu item '{item_name}' updated for '{restaurant_name}'."
        
        # If the item or restaurant doesn't exist, returns a message indicating the item was not found
        return f"Menu item '{item_name}' not found for '{restaurant_name}'."

    def delete_menu_item(self, restaurant_name, item_name):
        # Deletes a menu item from a restaurant's menu
        if restaurant_name in self.menus:
            for idx, item in enumerate(self.menus[restaurant_name]):
                if item['item_name'] == item_name:
                    # Deletes the item if found in the restaurant's menu
                    del self.menus[restaurant_name][idx]
                    return f"Menu item '{item_name}' deleted for '{restaurant_name}'."
        
        # If the item or restaurant doesn't exist, returns a message indicating the item was not found
        return f"Menu item '{item_name}' not found for '{restaurant_name}'."
