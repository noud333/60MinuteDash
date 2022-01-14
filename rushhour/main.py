from classes import Car, Board
import csv
import pandas
from functions import solve, load, save, visualize_csv
import time
from graph import graph


if __name__ == "__main__":

    start_time = time.time()

    # load the board via the load function
    board = load(filename="Rushhour12x12_7.csv", dimension=12)

    # solve the board
    solution = solve(board)
    print("Solved!!!")
    print(board.show())
    graph(board)

    # save the solution as a csv file with the name output
    save(solution, filename="output.csv")

    # time the program
    total_time = (time.time() - start_time)
    print("--- %s seconds ---" % (total_time))
    print(f"--- {len(solution[0])} steps ---")
    print(f"--- {len(solution[0])/total_time} steps per second ---")

    visualize_csv(output="output.csv", boardfile="Rushhour12x12_7.csv", dimension= 12)














