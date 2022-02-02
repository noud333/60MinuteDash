import copy
from .randomize import Simulate_random


class Hillclimber():
    """
    This algorithm takes a random solution and optimizes it by removing redundant moves.
    It does so recursively until no improvements are possible.
    Might result in a local optimum.
    """

    def __init__(self, board, solution=[[], []]):
        self.original_board = copy.deepcopy(board)
        self.solution = copy.deepcopy(solution)

    def simulate(self, n):
        """
        Simulate will generate a random solution 10 times and optimize the best solution.
        Will simulate this optimization process n times.
        Returns best solution out of all simulated solutions.
        """

        sols = []
        sols_len = []

        # generate a random board and optimizes it
        for i in range(n):
            board = self.original_board

            # simulate a random board
            random_solve = Simulate_random(board)
            solution = random_solve.simulate_n(10)[0]

            # optimize the random board
            hillclimber = Hillclimber(board, solution)
            solution = hillclimber.run()[0]
            sols.append(solution)
            sols_len.append(len(solution[0]))
            print(f"---Finished cycle {i + 1}, found solution of length {len(solution[0])}---")

        # return the solution with minimal length
        minimal_solution = 10000
        for sol in sols:
            if len(sol[0]) < minimal_solution:
                solution = sol
                minimal_solution = len(sol[0])
        return solution, sols_len

    def run(self):
        """ Run the algorithm """

        # go through all steps and remove redundant ones
        while self.remove_empty_spots():
            pass

        # check if current solution still results in a valid board
        is_valid, board = self.check_validity()
        return self.solution, board, is_valid

    def remove_empty_spots(self):
        """ Find all the steps where cars move back and forth and remove them from the solution """

        self.board = copy.deepcopy(self.original_board)

        self.empty_spots = {}

        positions_to_remove = self.find_redundant()

        # check redundant moves at the end
        for position in self.empty_spots:
            if self.empty_spots[position][0] != "X":
                positions_to_remove.append(self.empty_spots[position][1])

        return self.remove_redundant(positions_to_remove)

    def move(self, car, move):
        """ Find the empty and filled spots caused by a move from a car """

        if car.is_horizontal:
            # positive move: left empty, right filled
            if move > 0:
                empty = (car.row, car.col)
                filled = (car.row, car.col + car.length)
            # negative move: right empty, left filled
            else:
                empty = (car.row, car.col + car.length - 1)
                filled = (car.row, car.col - 1)
        else:
            # positive move: up empty, down filled
            if move > 0:
                empty = (car.row, car.col)
                filled = (car.row + car.length, car.col)
            # negative move: down empty, up filled
            else:
                empty = (car.row + car.length - 1, car.col)
                filled = (car.row - 1, car.col)

        # move the car
        self.board.move(car, move)

        return filled, empty

    def remove_redundant(self, redundant_moves):
        """ Removes the redundant moves from the solution """

        # remove the redundant moves
        if len(redundant_moves) > 0:
            # sort the moves to not break the indices
            redundant_moves.sort(reverse=True)

            # remove the values from the solution
            for i in redundant_moves:
                self.solution[0].pop(i)
                self.solution[1].pop(i)

            return True
        else:
            return False

    def check_validity(self):
        """ Check if every move in the solution is still a valid move """

        board = copy.deepcopy(self.original_board)
        is_valid = True

        # check all the moves
        for i in range(len(self.solution[0])):
            car, move = self.solution[0][i], self.solution[1][i]

            # check if current move is valid
            if not board.check_move(board.cars[car], move):
                is_valid = False

            # do the move
            board.move(board.cars[car], move)

        return is_valid, board

    def find_redundant(self):
        """ Look for redundant moves by keeping track of empty spots """

        positions_to_remove = []

        # look at every move in random solution
        for x in range(len(self.solution[0])):
            car, move = self.solution[0][x], self.solution[1][x]

            # keep track of spots that have changed for every move
            filled, empty = self.move(self.board.cars[car], move)

            # remove empty spot if it already exists
            # a car moving to the right twice in a row results in one empty spot for that car
            for key in self.empty_spots.keys():
                if self.empty_spots[key][0] == car and key != filled:
                    self.empty_spots.pop(key)
                    break

            self.empty_spots[empty] = (car, x)

            # check if the move can be removed
            positions_to_remove = self.is_redundant(positions_to_remove, filled, empty, car, x)

        return positions_to_remove

    def is_redundant(self, positions_to_remove, filled, empty, car, x):
        """ Check if new move is a redundant one, if so add it to the list """

        try:
            if self.empty_spots[filled][0] == car:
                # add current position and position of initial move to list
                positions_to_remove.append(self.empty_spots[filled][1])
                positions_to_remove.append(x)

                # clean up the empty_spots dict
                self.empty_spots.pop(filled)
                self.empty_spots.pop(empty)
            else:
                self.empty_spots.pop(filled)

        # in case a car does not exist in the dictionary
        except KeyError:
            pass

        return positions_to_remove
