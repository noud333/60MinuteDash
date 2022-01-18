from code.helpers import save
from code.algorithms.randomize import Random_solve, Simulate_random
from code.classes.board import Board
from code.visualisation.app import visualize_csv
import matplotlib.pyplot as plt
import csv
import statistics
import math

if __name__ == "__main__":

    # load the board via the load function
    board = Board(filename="Rushhour6x6_1.csv", dimension=6)
    
    # _______RANDOMIZE ALGORITHM__________
    random_solve = Random_solve(board)
    solution, solved_board = random_solve.run()
    # print specs of solution
    print(f"---Solved in {len(solution[0])} steps---")
    print(solved_board.show())
