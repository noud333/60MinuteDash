from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import pandas
import csv

def to_csv(solution_lengths, board_name):
    # save a list of solution lengths as a csv file
    df = pandas.DataFrame(data={"solution lengths": solution_lengths})
    df.to_csv(f"data/output/OptimizedRandom_{board_name}", sep=',', index=False)


def histogram(csv_file_name, title=""):
    # read the csv into a list
    data = []
    
    with open(f"data/output/{csv_file_name}") as file:
        reader = csv.DictReader(file)
        
        for line in reader:
            data.append(int(line["solution lengths"]))

    # make a matplotlib histogram
    plt.hist(data, bins=10)
    plt.xlabel("Steps needed until solved")
    plt.ylabel("Count")
    plt.title(title)
    plt.savefig(f"data/output/{csv_file_name[:-4]}.png")

    

def graph(board):
    plt.plot()
    plt.xticks(list(range(0, board.dimension + 1)))
    plt.yticks(list(range(0, board.dimension + 1)))
    for car in board.cars.values():
        if car.is_horizontal:
            rect = Rectangle((car.col,board.dimension - car.row - 1),car.length, 1)
        else:
            rect = Rectangle((car.col,board.dimension - car.row - car.length),1, car.length)
        if car.name == "X":
            rect.set_color("red")
        else:
            rect.set_color(list(np.random.choice(range(256), size=3)/256))
        rect.set_edgecolor("black")
        rect.set_linewidth(2)
        plt.gca().add_patch(rect)
    plt.savefig("test.png")

if __name__ == "__main__":
    histogram("OptimizedRandom_Rushhour9x9_6.csv")