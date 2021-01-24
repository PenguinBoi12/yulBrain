from .square import *

class Map:
    def __init__(self, id, name, squares):
        self._id = id
        self._name =  name
        self._squares = squares


    @property
    def id(self):
        return self._id


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, new_name):
        self._name = name


    @property
    def squares(self):
        return self._squares


    @squares.setter
    def squares(self, new_squares):
        self._squares = squares


    def square_value(self, line, column):
        return self._squares[line][column].value


    @staticmethod
    def parse(json_object):
        squares = []

        for square_col in json_object['square']:
            row_squares = []

            for square in square_col:
                row_squares.append(Square.parse(square))

            squares.append(row_squares)

        return Map(json_object['id'], json_object['name'], squares)
