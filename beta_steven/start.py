from classes import Car, Board
import csv
import pandas
from functions import solve
import time


if __name__ == "__main__":

    start_time = time.time()

    # create a board with the given dimension
    dimension = 12
    board = Board(dimension)

    # open the csv file and put the cars on the board
    with open(f"Rushhour{dimension}x{dimension}_7.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for x in csv_reader:
            car = Car(x["car"], x["orientation"], int(x["col"]) - 1, int(x["row"]) - 1, int(x["length"]))
            board.add(car)

    # solve the board
    solution = solve(board)
    print("Solved!!!")
    print(board.show())

    # save the solution as a csv file 
    df = pandas.DataFrame(data={"car": solution[0], "move": solution[1]})
    df.to_csv("output.csv", sep=',', index=False)

    # time the program
    total_time = (time.time() - start_time)
    print("--- %s seconds ---" % (total_time))
    print(f"--- {len(solution[0])} steps ---")
    print(f"--- {len(solution[0])/total_time} steps per second ---")














