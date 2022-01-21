from code.helpers import save
from code.classes.board import Board
from code.visualisation.app import visualize_csv
from code.algorithms.greedy import Greedy
from code.algorithms.randomize import Random_solve, Simulate_random
import matplotlib.pyplot as plt
import csv
import statistics
import math

if __name__ == "__main__":
    # load the board via the load function
    board = Board(filename="Rushhour6x6_1.csv", dimension=6)
    

    # solve the board and show the solution
    # greedy = Greedy(board)
    # solution, random_solved_board = greedy.run()
    # solution_length = len(solution[0])
    # print(f"--- Solution: {solution_length} ---")

    simulate_random = Simulate_random(board)
    solution, solved_board = simulate_random.simulate_n(10)
    
    # save the solution as a csv file with the name output
    save(solution, filename="output.csv")

    # show the result of the solution
    print(f"--- Random solution:")
    print(f"--- {len(solution[0])} steps ---")
 
    # visualize the solution making use of pygame
    visualize_csv(output="output.csv", original_board=board)
