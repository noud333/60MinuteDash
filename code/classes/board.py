import numpy as np
import math
import csv
from .car import Car

class Board:
    '''
    this class represents the playing board 
    '''
    def __init__(self, filename, dimension):
        # create an empty array
        self.dimension = dimension
        self.grid = np.array([['_'] * dimension] * dimension, dtype='U2')
        self.cars = {}
        self.load(filename)

    def load(self, filename):
        """ open the csv file and put the cars on the board """

        with open(f"data/gameboards/{filename}") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for x in csv_reader:
                car = Car(x["car"], x["orientation"], int(x["col"]) - 1, int(x["row"]) - 1, int(x["length"]))
                self.add(car)

    def show(self):
        """ show the board for visual aid """

        return self.grid

    def add(self, car):
        """ add a car onto the board """

        if car.is_horizontal:
            self.grid[car.row, car.col:car.col + car.length] = car.name
        else:
            self.grid[car.row:car.row + car.length, car.col] = car.name
        self.cars[car.name] = car
    
    # move a car in the given direction
    def move(self, car, direction):
        """ move a car in the given direction """

        if car.is_horizontal:
            self.grid[car.row, car.col:car.col + car.length] = '_'
            car.col = car.col + direction
            self.grid[car.row, car.col:car.col + car.length] = car.name
        else:
            self.grid[car.row:car.row + car.length, car.col] = '_'
            car.row = car.row + direction
            self.grid[car.row:car.row + car.length, car.col] = car.name
    
  
    def check_move(self, car, direction):
        """ check if a given move is valid """

        if direction < 0:

            if car.is_horizontal:
                
                # check if every spot the car wants to move to is empty
                for x in range(abs(direction)):
                    if self.grid[car.row, car.col + direction] != '_' or car.col + direction < 0 :
                        return False

            else:
                for x in range(abs(direction)):
                    if self.grid[car.row + direction, car.col]  != '_' or car.row + direction < 0:
                        return False

        # when the direction is positive, start at the end of the car
        elif direction > 0:

            if car.is_horizontal:
                for x in range(abs(direction)):
                    try:
                        # skip over the length of the car to start at the end
                        if self.grid[car.row, car.col + direction + car.length - 1] != '_' or car.col + direction > self.dimension:
                            return False
                    except IndexError:
                        return False

            else:
                for x in range(abs(direction)):
                    try:
                        # skip over the length of the car to start at the end
                        if self.grid[car.row + direction + car.length - 1, car.col]  != '_' or car.row + direction > self.dimension:
                            return False
                    except IndexError:
                        return False
        return True

    def finished(self):
        """ check whether the board is solved """
        return list(self.grid[math.ceil(self.dimension/2 - 1), self.dimension - 1]) == ['X']
