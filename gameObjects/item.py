# This class represents an item in the game

class Item:
    def __init__(self, itemName, itemType, iconUrl=None, specialAmount=0):
        self.itemName = itemName
        self.itemClass = itemClass
        self.itemIcon = iconUrl

        # the item's effectiveness, depending on the type of the item
        # for example, a potion with special amount of -3 deals 3hp to its target
        self.specialAmount = specialAmount


class Potion(Item):
    pass

class Weapon(Item):
    pass


# buff the player's attack? idk
class AmplifyingPotion(Potion):
    pass