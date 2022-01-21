from code.algorithms.randomize import Random_solve
from code.algorithms.greedy import Greedy
from code.classes.board import Board
from code.algorithms.breadth_first import Breadth_search

from code.helpers import save 
import time

if __name__ == "__main__":

    # load the board via the load function
    board = Board(filename="Rushhour6x6_3.csv", dimension=6)

    # _______RANDOMIZE ALGORITHM__________
    random_solve = Random_solve(board)
    solution, solved_board = random_solve.run()
    # print specs of solution
    print(f"---Solved Random in {len(solution[0])} steps---")
    print(solved_board.show())

    # _______GREEDY ALGORITHM_____________
    greedy_solve = Greedy(board)
    greedy_solution, greedy_board = greedy_solve.run()
    print(f"---Solved Greedy in {len(greedy_solution[0])} steps---")
    print(greedy_board.show())

    # _______BREADTH SEARCH ALGORITHM_____________
    start_time = time.time()
    breadth_solve = Breadth_search(board)
    solution, solved_board, unique_boards = breadth_solve.run()
    print(f"---Solved Breadth Search in {len(solution[0])} steps---")
    print(f"Total time = {time.time() - start_time}")
    print(f"Unique boards checked = {unique_boards}")

    save(solution, filename="output.csv")
