"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    items_with_count = {}
    for idr in set(items):
        items_with_count[idr] = items.count(idr)
    return items_with_count


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    for item in set(items):
        if item in inventory:
            count = inventory[item]
            inventory[item] = count + items.count(item)
        else:
            inventory[item] =   items.count(item)
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """
    for item in set(items):
        if item in inventory:
            value = inventory[item]
            if value >= items.count(item): 
                inventory[item] = value - items.count(item)
            else:
                inventory[item] = value - value
        else:
            pass
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
        return inventory
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """
    items = inventory.items()
    new_list = []
    for item in items:
        idr = list(item)
        if idr[-1]!=0:
            new_list.append(tuple(idr))
    return new_list
