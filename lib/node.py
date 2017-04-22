

class Node(object):
    def __init__(self):
        self.__north = None
        self.__south = None
        self.__east = None
        self.__west = None
        self.__visited = 0

    @property
    def north(self):
        return self.__north

    @north.setter
    def north(self, north):
        self.__north = north

    @property
    def south(self):
        return self.__south

    @south.setter
    def south(self, south):
        self.__south = south

    @property
    def east(self):
        return self.__east

    @east.setter
    def east(self, east):
        self.__east = east

    @property
    def west(self):
        return self.__west

    @west.setter
    def west(self, west):
        self.__west = west

    @property
    def visited(self):
        return self.__visited

    @visited.setter
    def visited(self, mark: int):
        self.__visited = mark

    def __str__(self) -> str:
        return str(self.__visited)