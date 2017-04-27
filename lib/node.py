import binascii
import os

class Node(object):
    """
    Node data structure
    """
    def __init__(self):
        self.__north = None
        self.__south = None
        self.__east = None
        self.__west = None
        self.__degree = 0
        self.__visited = 0
        self.__key = binascii.hexlify(os.urandom(32))

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
    def degree(self) -> int:
        return self.__degree

    @degree.setter
    def degree(self, deg: int):
        self.__degree = deg

    @property
    def visited(self):
        return self.__visited

    @visited.setter
    def visited(self, mark: int):
        self.__visited = mark

    @property
    def key(self):
        return self.__key

    def isNorthOf(self, node):
        return self.__south is node

    def isSouthOf(self, node):
        return self.__north is node

    def isEastOf(self, node):
        return self.__west is node

    def isWestOf(self, node):
        return self.__east is node

    def __eq__(self, other) -> bool:
        return self.key == other.key

    def __str__(self) -> str:
        return str(self.__visited)