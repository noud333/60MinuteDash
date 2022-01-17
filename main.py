from code.helpers import save
from code.algorithms.randomize import random_solve
from code.classes.board import Board
from code.visualisation.app import visualize_csv
import time


if __name__ == "__main__":
    
    start_time = time.time()

    # load the board via the load function
    board = Board(filename="Rushhour6x6_1.csv", dimension=6)

    # solve the board
    solution, random_solved_board = random_solve(board)
    print("Solved!!!")
    print(random_solved_board.show())

    # save the solution as a csv file with the name output
    save(solution, filename="output.csv")

    # time the program
    total_time = (time.time() - start_time)
    print("--- %s seconds ---" % (total_time))
    print(f"--- {len(solution[0])} steps ---")
    print(f"--- {len(solution[0])/total_time} steps per second ---")

    visualize_csv(output="output.csv", original_board=board)
