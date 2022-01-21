from code.algorithms.breadth_Noud import Breadth
from code.algorithms.randomize import Random_solve
from code.algorithms.greedy import Greedy
from code.classes.board_temp_noud import Board
import time

if __name__ == "__main__":

    # load the board via the load function
    board = Board(filename="Rushhour6x6_3.csv", dimension=6, local_save = True)

    # print(board.show())

    # # _______RANDOMIZE ALGORITHM__________
    # random_solve = Random_solve(board)
    # solution, solved_board = random_solve.run()
    # # print specs of solution
    # print(f"---Solved Random in {len(solution[0])} steps---")
    # print(solved_board.show())

    # # _______GREEDY ALGORITHM_____________
    # greedy_solve = Greedy(board)
    # greedy_solution, greedy_board = greedy_solve.run()

    # print(f"---Solved Greedy in {len(greedy_solution[0])} steps---")
    # print(greedy_board.show())

    cars= len(board.cars)
    dim = board.dimension

    begin = time.time()
    breadth_solve = Breadth(board, prune_size= 5000)#cars*(dim**2))
    breadth_solution, breadth_state = breadth_solve.run()
    end = time.time()
    print(breadth_solution)
    print(len(breadth_solution[0]), "length")
    print(breadth_state)
    print(end-begin)