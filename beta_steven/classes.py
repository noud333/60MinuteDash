import numpy as np


class Car:
    '''
    this class represents each individual car
    the cars can then be added onto the board
    '''
    def __init__(self, name, orientation, col, row, length):
        self.name = name
        self.orientation = orientation
        self.col = col
        self.row = row
        self.length = length


class Board:
    '''
    this class represents the playing board 
    '''
    def __init__(self, dimension):
        # create an empty array
        self.dimension = dimension
        self.grid = np.array([['_'] * dimension] * dimension, dtype='U2')
        self.cars = {}

    def show(self):
        """ show the board for visual aid """

        return self.grid

    def add(self, car):
        """ add a car onto the board """

        if car.orientation == "H":
            self.grid[car.row, car.col:car.col + car.length] = car.name
        elif car.orientation == "V":
            self.grid[car.row:car.row + car.length, car.col] = car.name
        self.cars[car.name] = car
    
    # move a car in the given direction
    def move(self, car, direction):
        """ move a car in the given direction """

        if car.orientation == "H":
            self.grid[car.row, car.col:car.col + car.length] = '_'
            car.col = car.col + direction
            self.grid[car.row, car.col:car.col + car.length] = car.name
        elif car.orientation == "V":
            self.grid[car.row:car.row + car.length, car.col] = '_'
            car.row = car.row + direction
            self.grid[car.row:car.row + car.length, car.col] = car.name
    
  
    def check_move(self, car, direction):
        """ check if a given move is valid """

        if direction < 0:

            if car.orientation == "H":
                
                # check if every spot the car wants to move to is empty
                for x in range(abs(direction)):
                    if self.grid[car.row, car.col + direction] != '_' or car.col + direction < 0 :
                        return False

            elif car.orientation == "V":
                for x in range(abs(direction)):
                    if self.grid[car.row + direction, car.col]  != '_' or car.row + direction < 0:
                        return False

        # when the direction is positive, start at the end of the car
        elif direction > 0:

            if car.orientation == "H":
                for x in range(abs(direction)):
                    try:
                        # skip over the length of the car to start at the end
                        if self.grid[car.row, car.col + direction + car.length - 1] != '_' or car.col + direction > self.dimension:
                            return False
                    except IndexError:
                        return False

            elif car.orientation == "V":
                for x in range(abs(direction)):
                    try:
                        # skip over the length of the car to start at the end
                        if self.grid[car.row + direction + car.length - 1, car.col]  != '_' or car.row + direction > self.dimension:
                            return False
                    except IndexError:
                        return False
        return True
