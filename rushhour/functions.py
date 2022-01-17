import csv
import random
import pandas
import math
from classes import Car, Board
from graph import App

def load(filename, dimension):

    # create a board with the given dimension
    board = Board(dimension)

    # open the csv file and put the cars on the board
    with open(f"files/gameboards/{filename}") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for x in csv_reader:
            car = Car(x["car"], x["orientation"], int(x["col"]) - 1, int(x["row"]) - 1, int(x["length"]))
            board.add(car)
    return board


def save(solution, filename):

    # save the solution as a csv file 
    df = pandas.DataFrame(data={"car": solution[0], "move": solution[1]})
    df.to_csv(f"files/output/{filename}", sep=',', index=False)


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

def visualize_csv(output, boardfile, dimension):
    """ perfroms moves in output on a boardfile """

    # load in the board
    board = load(boardfile, dimension)
    autos = []

    # add the initial state to the list 
    state = {}
    for car in board.cars.values():
        state[car.name] = {"row" : car.row, "col" : car.col, "length" : car.length, "is_horizontal" : car.is_horizontal}

    with open(f"files/output/{output}") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for step in csv_reader:
            state = {}
            board.move(board.cars[step["car"]], int(step["move"]))

            for car in board.cars.values():
                state[car.name] = {"row" : car.row, "col" : car.col, "length" : car.length, "is_horizontal" : car.is_horizontal}
            
            autos.append(state)
            
    # start the app
    app = App(dimension, autos)
    app.run()
     