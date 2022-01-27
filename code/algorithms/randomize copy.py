"""
This algorithms solves the rush hour game via random moves.
"""
import random
import copy
from xxlimited import new
from ..classes.board import Board


    
class Random_solve():
    """ Solves the board with random moves """

    def __init__(self, board,weights = []):
        self.original_board = board
        self.board = copy.deepcopy(board)

        # save the solution in a list of two lists
        self.solution = [[],[]]

        if len(weights) == 0:
            self.weights = []
            for car in self.original_board.cars.keys():
                self.weights.append(1)
        else:
            self.weights = weights

    def run(self):
        # try random moves until the red car is in the proper position
        while not self.board.finished():

            # select a random_car to move
            random_car = random.choices(list(self.board.cars.values()), self.weights)[0]
            random_direction = random.choice([-1,1])

            # only make the move if the move is valid
            if self.board.check_move(random_car, random_direction):
                self.board.move(random_car, random_direction)
                self.solution[0].append(random_car.name)
                self.solution[1].append(random_direction)

        return self.solution, self.board

class Simulate_random(Random_solve):

    def simulate_n(self, iterations):
        smallest_solution = 10000000
        best_board = self.board

        for x in range(iterations):
            new_solutions = {}

            for y in range(0, 100):
                self.board = copy.deepcopy(self.original_board)
                
                if x >= 1:
                    weights = list(cars.values())
                else:
                    weights = []

                new_random = Random_solve(self.board, weights)

                new_solution = []
                new_solution, new_board = new_random.run()

                new_solutions[len(new_solution[0])] = new_solution

                if len(new_solution[0]) < smallest_solution:
                    best_board = new_board
                    best_solution = new_solution
                    smallest_solution = len(new_solution[0])
            
                print("Solution #", y, " Length: ", len(new_solution[0]))

            new_solutions = sorted(new_solutions.items())
            new_solutions = new_solutions[:10]


            cars = {}
            for letter in best_board.cars.keys():
                cars[letter] = 0

            for solution in new_solutions:
                for item in solution[1]:
                    
                    for letter in item:
                        if type(letter) == str:
                            if letter in cars:
                                cars[letter] += 1
                            else:
                                cars[letter] = 1

        return best_solution, best_board

if __name__ == "__main__":

    board = Board(filename="Rushhour6x6_2.csv", dimension=6)
    random_solve = Random_solve(board)
    solution, solved_board = random_solve.run()
    # print specs of solution
    print(f"---Solved Random in {len(solution[0])} steps---")
    print(solved_board.show())