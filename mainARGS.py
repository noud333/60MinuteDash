from code.algorithms.randomize import Random_solve, Simulate_random
from code.algorithms.greedy import Greedy
from code.classes.board import Board
from code.algorithms.breadth_first import Breadth_search
from code.algorithms.optimizer import Optimizer

from code.helpers import save 
import time
import argparse


# setup the command line input
parser = argparse.ArgumentParser(description="Solve rush-hour")
parser.add_argument("-b", "--board", type=int, help="Run one of the standard boards", choices=range(1, 8), metavar="[1-7]")
parser.add_argument("-r", "--random", type=int, help="Run a random board with the given dimension", metavar="dimension")
parser.add_argument(
    "-a", "--algorithm", default="random", metavar="algorithm",
    choices=("random", "breadth-first", "optimized-random"),
    help="Solve a board using the random, breadth-first or optimized-random algorithm")
parser.add_argument("-o", "--output", type=str, help="Save output solution as a .csv", metavar="outputname")
parser.add_argument("-t", "--timed", type=bool, default=False, help="Time the algorith", metavar="[True/False]")

args = parser.parse_args()


if __name__ == "__main__":

    # load the board via the load function
    if args.b is not None:
        if args.b in range(1, 4):
            board = Board(filename=f"Rushhour6x6_{args.b}.csv", dimension=6)
        elif args.b in range(4, 7):
            board = Board(filename=f"Rushhour9x9_{args.b}.csv", dimension=9)
        elif args.b == 7:
            board = Board(filename="Rushhour6x6_7.csv", dimension=12)
    elif args.r:
        # make a random board
        pass

    if args.b is None and args.r is None:
        # PROBLEM
        print("ERROR")

    # run the given algorithm
    if args.a is not None:
        if args.a == "random":
            # _______RANDOMIZE ALGORITHM__________
            start_time = time.time()
            random_solve = Simulate_random(board)
            solution, solved_board = random_solve.simulate_n(10)
            # print specs of solution
            print(f"---Solved Random in {len(solution[0])} steps---")
            if args.t:
                print(f"Total time = {time.time() - start_time}")
            print(solved_board.show())

    elif args.a == "breadth-first":
        # _______BREADTH SEARCH ALGORITHM_____
        start_time = time.time()
        breadth_solve = Breadth_search(board)
        solution, solved_board, unique_boards, boards_checked = breadth_solve.run()
        print(f"---Solved Breadth Search in {len(solution[0])} steps---")
        if args.t:
            print(f"Total time = {time.time() - start_time}")
        print(f"Unique boards checked = {unique_boards}")
        print(f"Boards checked {boards_checked}")

    elif args.a == "optimized-random":
        # _______OPTIMIZED RANDOM ALGORITHM___
        start_time = time.time()
        sols = []
        minimum = 1000000
        min_at = 0
        for i in range(10):
            random_solve = Simulate_random(board)
            solution, solved_board = random_solve.simulate_n(10)
            optimizer = Optimizer(board, solution)
            solution, solved_board, is_valid = optimizer.run()
            sols.append(solution)
            if len(solution[0]) < minimum:
                minimum = len(solution[0])
                min_at = i
        solution = sols[min_at]
        # print specs of solution
        print(f"---Solved Optimized Random in {len(solution[0])} steps---")
        if args.t:
            print(f"Total time = {time.time() - start_time}")

    # save the output if requested
    if args.o:
        output_name = f"{args.o}.csv"
        save(solution, filename=output_name)
