from abc import ABC, abstractmethod


class Randomiser(ABC):

    @staticmethod
    @abstractmethod
    def randomise():
        pass


class ItemRandomiser(Randomiser):

    @staticmethod
    def randomise():
        pass


class MobRandomiser(Randomiser):
    @staticmethod
    def randomise():
        pass
