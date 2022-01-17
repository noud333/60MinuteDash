"""
Tries to solve a Rush Hour game in as few steps as possible
"""

from game import Game
from visual import App
import time


start = time.time()
# test code
game = Game(6, "Rushhour6x6_1.csv")
random_sol = game.solve_random()
game.save_output(random_sol, "Random_12x12")
end = time.time()
print(end - start)

# prepare to use the visual app
states = game.output_to_states(random_sol)
app = App(6)
# add all states
for state in states:
    app.add_state(state)
app.run()
