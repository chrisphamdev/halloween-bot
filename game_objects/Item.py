# This class represents an item in the game


class Item:
    def __init__(self, item_name: str, item_class, icon_url=None, special_amount=0):
        self.item_name = item_name
        self.item_class = item_class
        self.item_icon = icon_url

        # the item's effectiveness, depending on the type of the item
        # for example, a potion with special amount of -3 deals 3hp to its target
        self.special_amount = special_amount

