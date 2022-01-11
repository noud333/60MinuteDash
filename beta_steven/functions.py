import csv
import random
import pandas
import math



def solve(board):
    
    # save the solution in a list of two lists
    solution = [[],[]]

    # try random moves until the red car is in the proper position
    while list(board.board[math.ceil(board.dimension/2 - 1), board.dimension - 2:board.dimension]) != ['X', 'X']:
        random_car = random.choice(list(board.cars.keys()))
        random_direction = random.choice([-1,1])

        # only make the move if the move is valid
        if board.check_move(board.cars[random_car], random_direction):
            board.move(board.cars[random_car], random_direction)
            solution[0].append(random_car)
            solution[1].append(random_direction)

    return solution