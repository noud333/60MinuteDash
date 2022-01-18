"""
This algorithms solves the rush hour game via random moves.
"""
import random
import copy


    
class Random_solve():
    """ Solves the board with random moves """

    def __init__(self, board):
        self.original_board = board
        self.board = copy.deepcopy(board)
        # save the solution in a list of two lists
        self.solution = [[],[]]

    def run(self):
        # try random moves until the red car is in the proper position
        while not self.board.finished():

            # select a random_car to move
            random_car = random.choice(list(self.board.cars.keys()))
            random_direction = random.choice([-1,1])

            # only make the move if the move is valid
            if self.board.check_move(self.board.cars[random_car], random_direction):
                self.board.move(self.board.cars[random_car], random_direction)
                self.solution[0].append(random_car)
                self.solution[1].append(random_direction)

        return self.solution, self.board

class Simulate_random(Random_solve):

    def simulate_n(self, repeats):
        smallest_solution = 10000000
        best_board = self.board

        for x in range(0, repeats):
            self.board = copy.deepcopy(self.original_board)
            self.solution = [[],[]]
            new_solution, new_board = self.run()
            
            if len(new_solution[0]) < smallest_solution:
                best_board = new_board
                best_solution = new_solution
                smallest_solution = len(new_solution[0])
        
            print("Solution #", x, " Length: ", len(new_solution[0]))

        return best_solution, best_board