"""
Contains the Board class for a Rush Hour game
"""

from car import Car
import csv

class Board():
    """ An nxn Board for a Rush Hour game """

    def __init__(self, n):
        self.n = n
        self.grid = self.empty_grid()
        self.cars = {}

    def empty_grid(self):
        """ Creates an empty nxn grid, so filled with 0's """
        grid = {}
        for row_num in range(self.n):
            new_row = {}
            for col_num in range(self.n):
                new_row[col_num + 1] = "0"
            grid[row_num + 1] = new_row
        return grid
    
    def fill_board(self, board_file):
        """ Uses a .csv file to place cars on the board """
        with open(f"files/gameboards/{board_file}") as file:
            reader = csv.reader(file)
            
            # skip the header
            next(reader, None)

            # store each car
            for row in reader:
                new_car = Car(row[0], row[1], int(row[2]), int(row[3]), int(row[4]))
                self.cars[new_car.get_name()] = new_car

            # update the grid
            self.update_grid()
    
    def update_grid(self):
        """ Updates the grid by replacing all cars """
        self.grid = self.empty_grid()
        for car in self.cars.values():
            for step in range(car.length):
                if car.is_horizontal:
                    self.grid[car.row][car.col + step] = car.name
                else:
                    self.grid[car.row + step][car.col] = car.name
    
    def show_board(self):
        """ Prints the board in its current state using two characters per name """
        # all the cars
        for row in self.grid.values():
            for char in row.values():
                if len(char) == 1:
                    name = " " + char
                else: 
                    name = char
                print(name, end=" ")
            print()
        
    def move(self, car_name, steps):
        """ Move a car """
        
        # get the car with its location
        car = self.cars[car_name]
        row, col = car.get_location()

        # the carlength should only be added if moving down or right
        if steps < 0:
            carlength = 1
        else:
            carlength = car.length

        # check if the move is valid
        if car.is_horizontal:
             # check if the car stays inside the grid
            if col + steps < 1 or col + steps + car.length - 1 > self.n:
                return False
            for i in range(steps):
                if self.grid[row][col + carlength + i] != "0":
                    return False
        else:
            # check if the car stays inside the grid
            if row + steps < 1 or row + steps + car.length - 1 > self.n:
                return False
            for i in range(steps):
                if self.grid[row + carlength + i][col] != "0":
                    return False

        # move the car and update the grid
        car.move(steps)
        self.update_grid()
        return True

    def is_finished(self):
        """ The game is finished if car X is next to the exit """
        return self.cars["X"].col + 1 == self.n