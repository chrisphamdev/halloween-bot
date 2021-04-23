# This class represent a player (Discord user)
# The player ID will be fetched from the userID

from tinydb import TinyDB, Query


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.inventory = []

    # add an item of the class Item to the player's inventory
    def item_acquired(self, item):
        self.inventory += [item]

    # TO BE IMPLEMENTED
    # This function will update the player's inventory to the database  
    def update_db(self):
        pass
