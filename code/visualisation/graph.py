from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


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
