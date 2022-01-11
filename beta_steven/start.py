import numpy as np
import csv
import random

class Car:
    def __init__(self, name, orientation, col, row, length):
        self.name = name
        self.orientation = orientation
        self.col = col
        self.row = row
        self.length = length

class Board:
    def __init__(self, dimension):
        self.board = np.array([['_'] * dimension] * dimension)
        self.cars = {}

    def show(self):
        return self.board

    def add(self, car):
        if car.orientation == "H":
            self.board[car.row, car.col:car.col + car.length] = car.name
        elif car.orientation == "V":
            self.board[car.row:car.row + car.length, car.col] = car.name
        self.cars[car.name] = car
    
    def move(self, car, direction):
        if car.orientation == "H":
            self.board[car.row, car.col:car.col + car.length] = '_'
            car.col = car.col + direction
            self.board[car.row, car.col:car.col + car.length] = car.name
        elif car.orientation == "V":
            self.board[car.row:car.row + car.length, car.col] = '_'
            car.row = car.row + direction
            self.board[car.row:car.row + car.length, car.col] = car.name
    
    def check_move(self, car, direction):
        if car.orientation == "H":
            for x in range(abs(direction)):
                if self.board[car.row, car.col + direction] != '_' or car.col + direction < 0 :
                    return False
        elif car.orientation == "V":
            for x in range(abs(direction)):
                if self.board[car.row + direction, car.col]  != '_' or car.row + direction < 0:
                    return False
        return True

def solve(board):
    while list(board.board[2, 4:6]) != ['X', 'X']:
        random_car = random.choice(list(board.cars.keys()))
        random_direction = random.choice([-1,1])
        if board.check_move(board.cars[random_car], random_direction):
            board.move(board.cars[random_car], random_direction)
            print(f"Moved {random_car} by {random_direction}")
        print(f"Unable to move {random_car} by {random_direction}")
        print(board.show())

if __name__ == "__main__":


    board = Board(6)
    with open("Rushhour6x6_1.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for x in csv_reader:
            car = Car(x["car"], x["orientation"], int(x["col"]) - 1, int(x["row"]) - 1, int(x["length"]))
            board.add(car)

    solve(board)
    print(board.show())














