# This class represent a monster that players can participate in fighting
# All default values are as specified

class Mob:
    def __init__(self, monster_name, monster_type, monster_hp=100, monster_dmg=10, monster_icon_url=None):
        self.monsterName = monster_name
        self.monsterType = monster_type
        self.monsterHP = monster_hp
        self.monsterDMG = monster_dmg
        self.monsterIcon = monster_icon_url
