from code.algorithms.randomize import Random_solve, Simulate_random
from code.algorithms.greedy import Greedy
from code.classes.board import Board
from code.algorithms.breadth_first import Breadth_search
from code.algorithms.depth_first import Depth_search
from code.algorithms.hillclimber import Optimizer

from code.helpers import save 
import time

if __name__ == "__main__":

    # load the board via the load function
    board = Board(filename="Rushhour12x12_7.csv", dimension=12)

    # # _______DEPTH ALGORITHM___________
    # begin = time.time()
    # depth_solve = Depth_search(board, 10000)
    # solution, solved_board, boards_checked = depth_solve.run()
    # end = time.time()
    # # print specs of solution
    # print(f"---Solved Depth in {len(solution[0])} steps---")
    # print(f"---Boards checked {boards_checked}")
    # print(f"Total time = {end - begin}")
    # # print(solved_board.show())


    # # _______RANDOMIZE ALGORITHM__________
    # random_solve = Simulate_random(board)
    # solution, solved_board = random_solve.simulate_n(10)
    # # print specs of solution
    # print(f"---Solved Random in {len(solution[0])} steps---")
    # print(solved_board.show())

    # # _______GREEDY ALGORITHM_____________
    # greedy_solve = Greedy(board)
    # greedy_solution, greedy_board = greedy_solve.run()
    # print(f"---Solved Greedy in {len(greedy_solution[0])} steps---")
    # print(greedy_board.show())

    # # _______BREADTH SEARCH ALGORITHM_____________
    # start_time = time.time()
    # breadth_solve = Breadth_search(board)
    # solution, solved_board, unique_boards, boards_checked = breadth_solve.run()
    # print(f"---Solved Breadth Search in {len(solution[0])} steps---")
    # print(f"Total time = {time.time() - start_time}")
    # print(f"Unique boards checked = {unique_boards}")
    # print(f"Boards checked {boards_checked}")


    for i in range(100):

        # _______OPTIMIZE ALGORITHM__________
        random_solve = Simulate_random(board)
        solution, solved_board = random_solve.simulate_n(10)
        # print specs of solution
        print(f"---Solved Random in {len(solution[0])} steps---")
        # print(solved_board.show())

        optimizer = Optimizer(board, solution)
        solution, solved_board, is_valid = optimizer.run()
        # print specs of solution
        print(f"---Solved Optimizer {i} in {len(solution[0])} steps---")
        print(solved_board.show())
        print(f"The optimized solution: {is_valid}")

        save(solution, filename=f"output_{i}.csv")
