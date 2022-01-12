"""
Contains the Board class for a Rush Hour game
"""

from car import Car
import csv
from matplotlib import pyplot as plt

class Board():
    """ An nxn Board for a Rush Hour game """

    def __init__(self, n):
        self.n = n
        self.grid = self.empty_grid()
        self.cars = {}

    def empty_grid(self):
        """ Creates an empty nxn grid, so filled with _'s """
        grid = {}
        for row_num in range(self.n):
            new_row = {}
            for col_num in range(self.n):
                new_row[col_num + 1] = "_"
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
            self.hard_update_grid()
    
    def hard_update_grid(self):
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

        if self.move_is_valid(car, steps):
            # move the car and update the grid
            self.remove_from_grid(car)
            car.move(steps)
            self.place_at_grid(car)
            return True
        return False
    
    def move_is_valid(self, car, steps):
        """ Check if a move is valid """
        row, col = car.get_location()
        going_bottomright = steps >= 0

        if car.is_horizontal:
             # check if the car stays inside the grid
            if col + steps < 1 or col + steps + car.length - 1 > self.n:
                return False

            # check the path that the car will follow
            if not going_bottomright:
                for i in range(0, steps, -1):
                    if self.grid[row][col + i - 1] != "_":
                        return False
            else:
                for i in range(0, steps, 1):
                    if self.grid[row][col + i + car.length] != "_":
                        return False
        else:
            # check if the car stays inside the grid
            if row + steps < 1 or row + steps + car.length - 1 > self.n:
                return False

            # check the path that the car will follow
            if not going_bottomright:
                for i in range(0, steps, -1):
                    if self.grid[row + i - 1][col] != "_":
                        return False
            else:
                for i in range(0, steps, 1):
                    if self.grid[row + i + car.length][col] != "_":
                        return False
        return True

    def remove_from_grid(self, car):
        """ Removes a car from the grid """
        length = car.length
        row, col = car.get_location()
        for step in range(length):
            if car.is_horizontal:
                self.grid[row][col + step] = "_"
            else:
                self.grid[row + step][col] = "_"

    def place_at_grid(self, car):
        """ Places a car at the grid """
        length = car.length
        row, col = car.get_location()
        name = car.get_name()
        for step in range(length):
            if car.is_horizontal:
                self.grid[row][col + step] = name
            else:
                self.grid[row + step][col] = name

    def is_finished(self):
        """ The game is finished if car X is next to the exit """
        return self.cars["X"].col + 1 == self.n

    def matplotlib_state(self, file_name):
        """ Uses matplotlib to show the current state """
        plt.axes()
        bg = plt.Rectangle((0, -1 * self.n), self.n, self.n, fc="grey")
        plt.gca().add_patch(bg)
        # add cars
        for car in self.cars.values():
            if car.is_horizontal:
                new = plt.Rectangle((car.col - 1, -1 * car.row), car.length, 1, fc="blue", ec="black")
                plt.gca().add_patch(new)
            else:
                new = plt.Rectangle((car.col - 1, -1 * car.row - car.length + 1), 1, car.length, fc="blue", ec="black")
                plt.gca().add_patch(new)
        # put the rec car over all
        car = self.cars["X"]
        red = plt.Rectangle((car.col - 1, -1 * car.row), car.length, 1, fc="red", ec="black")
        plt.gca().add_patch(red)

        plt.axis("scaled")
        plt.savefig(file_name)