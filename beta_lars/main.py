"""
Tries to solve a Rush Hour game in as few steps as possible
"""

from game import Game
from visual import App
import time

start = time.time()
# test code
game = Game(12, "Rushhour12x12_7.csv")
random_sol = game.solve_random()
game.save_output(random_sol, "Random_12x12")
end = time.time()
print(end - start)

game.board.matplotlib_state("files/output/test.png")

app = App(12, game.board.cars)
app.run()
