from Mob import Mob
from Boss import Boss
from Item import Item
from Randomiser import MobRandomiser, ItemRandomiser


class ObjectFactory:

    @staticmethod
    def create(object_name: str):
        if object_name == 'boss':
            return Boss()
        elif object_name == 'mob':
            return Mob(MobRandomiser.randomise())
        elif object_name == 'item':
            return Item(ItemRandomiser.randomise())
