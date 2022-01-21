import numpy as np
import math
import csv
from .car import Car

class Board:
    '''
    this class represents the playing board 
    '''
    def __init__(self, filename, dimension, local_save = False):
        # create an empty array
        self.dimension = dimension
        self.grid = np.array([['_'] * dimension] * dimension, dtype='U2')
        self.cars = {}
        self.load(filename)
        self.local_save = local_save
        if self.local_save:
            self.solution = [[],[]] 

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
        
        if self.local_save:
            self.solution[0].append(car.name)
            self.solution[1].append(direction)
    
  
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

    def get_neighbor(self, car, going_bottom_right):
        """ Returns the car in the given direction """ 
        try:
            if going_bottom_right:
                if car.is_horizontal:
                    neighbor = self.grid[car.row, car.col + car.length]
                else:  
                    neighbor = self.grid[car.row + car.length, car.col]
                
            else:
                if car.is_horizontal and car.col != 0:
                    neighbor = self.grid[car.row, car.col - 1]
                elif not car.is_horizontal and car.row != 0:
                    neighbor = self.grid[car.row - 1, car.col]
                else:
                    return None
            neighbor = self.cars[neighbor]
        except IndexError:
            neighbor = None
        
        return neighbor

    def finished(self):
        """ Check whether the board is solved """
        return list(self.grid[math.ceil(self.dimension/2 - 1), self.dimension - 1]) == ['X']

    def get_moves(self):
        """ Gives all possible moves """
        move_list = [[], []]
        for car in self.cars.values():
            if self.check_move(car, 1):
                move_list[0].append(car)
                move_list[1].append(1)

            if self.check_move(car, -1):
                move_list[0].append(car)
                move_list[1].append(-1)
 
        return move_list