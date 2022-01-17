"""
This algorithms solves the rush hour game via random moves.
"""
import random
import copy


    
def random_solve(board):
    """ Solves the board with random moves """

    board = copy.deepcopy(board)
    # save the solution in a list of two lists
    solution = [[],[]]

    # try random moves until the red car is in the proper position
    while not board.finished():

        # select a random_car to move
        random_car = random.choice(list(board.cars.keys()))
        random_direction = random.choice([-1,1])

        # only make the move if the move is valid
        if board.check_move(board.cars[random_car], random_direction):
            board.move(board.cars[random_car], random_direction)
            solution[0].append(random_car)
            solution[1].append(random_direction)

    return solution, board
