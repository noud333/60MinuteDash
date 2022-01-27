from code.algorithms.randomize import Simulate_random
from code.classes.board import Board
from code.algorithms.breadth_first import Breadth_search
from code.algorithms.optimizer import Optimizer

from code.visualisation.app import visualize_csv
from code.visualisation.graph import to_csv, histogram
from code.helpers import save 
import time
import argparse


def main(args):
    # load the board via the load function
    if args.board is not None:
        board = Board(filename=args.board[0], dimension=int(args.board[1]))
        

    # run the given algorithm
    if args.algorithm is not None:
        if args.algorithm == "random":
            # _______RANDOMIZE ALGORITHM__________
            start_time = time.time()
            random_solve = Simulate_random(board)
            solution, solved_board = random_solve.simulate_n(10)
            # print specs of solution
            print(f"---Solved Random in {len(solution[0])} steps---")
            if args.timed:
                print(f"Total time = {time.time() - start_time}")
            print(solved_board.show())

        elif args.algorithm == "breadth-first":
            # _______BREADTH SEARCH ALGORITHM_____
            start_time = time.time()
            breadth_solve = Breadth_search(board)
            solution, solved_board, unique_boards, boards_checked = breadth_solve.run()
            print(f"---Solved Breadth Search in {len(solution[0])} steps---")
            if args.timed:
                print(f"Total time = {time.time() - start_time}")
            print(f"Unique boards checked = {unique_boards}")
            print(f"Total boards checked = {boards_checked}")

        elif args.algorithm == "optimized-random":
            # _______OPTIMIZED RANDOM ALGORITHM___
            start_time = time.time()
            optimizer = Optimizer(board)
            solution, solution_lengths = optimizer.simulate(100)
            # print specs of solution
            print(f"---Solved Optimized Random in {len(solution[0])} steps---")
            if args.timed:
                print(f"Total time = {time.time() - start_time}")
            
            if args.output:
                to_csv(solution_lengths, args.board[0])

    # save the output if requested
    if args.output:
        output_name = f"{args.output}.csv"
        save(solution, filename=output_name)

        # visualize the solution if requested
        if args.visualize:
            visualize_csv(output_name, board)



if __name__ == "__main__":
    # setup the command line input
    parser = argparse.ArgumentParser(description="Solve rush-hour")
    parser.add_argument("-b", "--board", nargs=2, help="Run a boardfile", metavar=("filename", "dimension"), required=True)
    parser.add_argument(
        "-a", "--algorithm", default="random", metavar="algorithm",
        choices=("random", "breadth-first", "optimized-random"),
        help="Solve a board using the \"random\", \"breadth-first\" or \"optimized-random\" algorithm")
    parser.add_argument("-o", "--output", type=str, help="Save output solution as a .csv", metavar="outputname")
    parser.add_argument("-t", "--timed", action="store_true", help="Time the algorith")
    parser.add_argument("-v", "--visualize", action="store_true", help="Visualize the outputted solution")

    args = parser.parse_args()

    main(args)