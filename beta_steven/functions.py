import csv
import random
import pandas
import math
from classes import Car, Board


def load(filename, dimension):

    # create a board with the given dimension
    board = Board(dimension)

    # open the csv file and put the cars on the board
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for x in csv_reader:
            car = Car(x["car"], x["orientation"], int(x["col"]) - 1, int(x["row"]) - 1, int(x["length"]))
            board.add(car)
    return board


def save(solution, filename):

    # save the solution as a csv file 
    df = pandas.DataFrame(data={"car": solution[0], "move": solution[1]})
    df.to_csv(filename, sep=',', index=False)


def solve(board):
    
    # save the solution in a list of two lists
    solution = [[],[]]

    # try random moves until the red car is in the proper position
    while list(board.grid[math.ceil(board.dimension/2 - 1), board.dimension - 1]) != ['X']:

        # select a random_car to move
        random_car = random.choice(list(board.cars.keys()))
        random_direction = random.choice([-1,1])

        # only make the move if the move is valid
        if board.check_move(board.cars[random_car], random_direction):
            board.move(board.cars[random_car], random_direction)
            solution[0].append(random_car)
            solution[1].append(random_direction)

    return solution