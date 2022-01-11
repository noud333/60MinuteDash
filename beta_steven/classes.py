import numpy as np


# the car class
class Car:
    def __init__(self, name, orientation, col, row, length):
        self.name = name
        self.orientation = orientation
        self.col = col
        self.row = row
        self.length = length


# the board class
class Board:
    def __init__(self, dimension):
        # create an empty array
        self.dimension = dimension
        self.board = np.array([['_'] * dimension] * dimension, dtype='U1')
        self.cars = {}

    # show the board for visual aid
    def show(self):
        return self.board

    # add a car onto the board
    def add(self, car):
        if car.orientation == "H":
            self.board[car.row, car.col:car.col + car.length] = car.name
        elif car.orientation == "V":
            self.board[car.row:car.row + car.length, car.col] = car.name
        self.cars[car.name] = car
    
    # move a car in the given direction
    def move(self, car, direction):
        if car.orientation == "H":
            self.board[car.row, car.col:car.col + car.length] = '_'
            car.col = car.col + direction
            self.board[car.row, car.col:car.col + car.length] = car.name
        elif car.orientation == "V":
            self.board[car.row:car.row + car.length, car.col] = '_'
            car.row = car.row + direction
            self.board[car.row:car.row + car.length, car.col] = car.name
    
    # check if a given move is valid
    def check_move(self, car, direction):
        if direction < 0:
            if car.orientation == "H":
                for x in range(abs(direction)):
                    if self.board[car.row, car.col + direction] != '_' or car.col + direction < 0 :
                        return False
            elif car.orientation == "V":
                for x in range(abs(direction)):
                    if self.board[car.row + direction, car.col]  != '_' or car.row + direction < 0:
                        return False

        # when the direction is positive, start at the end of the car
        elif direction > 0:
            if car.orientation == "H":
                for x in range(abs(direction)):
                    try:
                        # skip over the length of the car to start at the end
                        if self.board[car.row, car.col + direction + car.length - 1] != '_' or car.col + direction > self.dimension:
                            return False
                    except IndexError:
                        return False
            elif car.orientation == "V":
                for x in range(abs(direction)):
                    try:
                        # skip over the length of the car to start at the end
                        if self.board[car.row + direction + car.length - 1, car.col]  != '_' or car.row + direction > self.dimension:
                            return False
                    except IndexError:
                        return False
        return True
