# This class represent a monster that players can participate in fighting
# All default values are as specified

class Monster:
    def __init__(self, monsterName, monsterType, monsterHP=100, monsterDMG=10, monsterIconURL=None):
        self.monsterName = monsterName
        self.monsterType = monsterType
        self.monsterHP = monsterHP
        self.monsterDMG = monsterDMG
        self.monsterIcon = monsterIconURL