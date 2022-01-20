"""breadth search algorithm"""

import copy

class Breadth():
    """
    Calculates the best solution for the game Rush Hour using the breadth search algorithm.
    """
    def __init__(self, board, prune_size= 10**10):
        # save the board
        self.original_board = board
        self.prune_size = prune_size

        # create a set with all known states of the board
        self.found_states = set()
        self.found_states.add(self.tostring(self.original_board.show()))

        self.list_of_boards = [board]
    
    def run(self, expected_steps = 1000):
        """ tries every possible step that can be made from a board and remove ones that have been seen previously """

        for i in range(expected_steps):
            # progress report
            print("Step:", i + 1, "Boards:", len(self.list_of_boards))

            # every valid new board is saved here
            new_boards = []
            
            # look at every board that can be reached in i amount of steps
            for new_board in self.list_of_boards:

                # look at which moves can be made from here
                moves = new_board.get_moves()

                # check every possible move
                for move_index in range(len(moves[0])):

                    # create a new board is the current state to move
                    temp_board = copy.deepcopy(new_board)

                    # do the move
                    temp_board.move(temp_board.cars[moves[0][move_index].name], moves[1][move_index])

                    # check for solution
                    if temp_board.finished():
                        return temp_board.solution, temp_board.show()

                    # change state of board into string
                    state = self.tostring(temp_board.show())

                    # check if current board is unique if so save it
                    if state not in self.found_states:
                        self.found_states.add(state)
                        new_boards.append(temp_board)
                    
                    if self.calc_heur(temp_board):
                        # check if nothing blocks red car
                        red_car = temp_board.cars["X"]

                        while True:
                            # move red car to finished state
                            temp_board.move(red_car, 1)

                            if temp_board.finished():
                                return temp_board.solution, temp_board.show()

            if len(new_boards) > self.prune_size and i % 5 == 0:
                heurs = {}
                
                for board in new_boards:
                    heurs[board] = self.pruner(board)
                
                sort_heurs = sorted(heurs.items(), key=lambda x: x[1])
                
                boards = []
                for i in range(self.prune_size):
                    boards.append(sort_heurs[i][0])
                self.list_of_boards = boards
                new_boards = []


            else:
                self.list_of_boards = new_boards
                new_boards = []
        return "Solution not found", f"expected_steps: {expected_steps}"

    def tostring(self, array):
        """ changes the board array to a string"""  
        array = array.tolist()

        string = ""

        for row in array:
            for value in row:
                string += value

        return string
    
    def calc_heur(self, board):
        """ check if anything stands in the way of the red car"""

        row = board.cars["X"].row

        for i in range(board.cars["X"].col + 2,board.dimension):

            if board.show()[row][i] != "_":
                return False
        return True
    
    def pruner(self, board):
        heur = 0

        row = board.cars["X"].row

        for i in range(board.cars["X"].col + 2,board.dimension):

            if board.show()[row][i] != "_":
                heur += 1

        return heur