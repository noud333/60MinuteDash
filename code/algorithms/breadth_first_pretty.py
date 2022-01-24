import copy


class Breadth_search():
    """
    Breath first algorithm making use of archive to save visited states.
    Makes use of prunning by cutting states with a score of 2 higher than the minimum.
    Due to optimising based on memory use, it may cause the best solution to be missed.
    """
    def __init__(self, board):

        # save the starting board in active boards
        self.board = copy.deepcopy(board)
        self.board.score = self.estimate(self.board)
        self.active_boards = [self.board]

        # save the boards that have already been visited and add the starting board to it
        self.visited_boards = {tuple(map(tuple, self.board.show()))}

        # count the number of steps it takes and the boards visited
        self.steps = 0
        self.unique_boards = 0

    def run(self):

        while True:

            # show the current layer the algorithm is at
            self.steps += 1
            print(f"Currently looking at step: {self.steps}, with {len(self.active_boards)} branches")

            # this is the pruning step
            self.active_boards = self.prune(self.active_boards)

            # make a copy of the active boards
            boards = self.active_boards[:]
            self.active_boards = []

            # for every board create branching paths
            for board in boards:

                # get every available move and create a new branch for every move
                available_moves = board.get_moves()
                for x in range(len(available_moves[0])):
                    current_board = self.create_branch(board, available_moves[0][x], available_moves[1][x])

                    # check if the board has already been visited
                    if not self.is_visited(current_board):
                        
                        # add the new board to the active boards for next iteration
                        self.add_board(current_board, available_moves[0][x], available_moves[1][x] )

                        # check if the victory condition has been met
                        if current_board.finished():
                            return current_board.solution, current_board, self.unique_boards

    def add_board(self, board, car, move):
        """add a new board to the active boards for next iteration"""
        self.unique_boards += 1
        board.score = self.estimate(board)
        self.active_boards.append(board)
        board.solution[0].append(car)
        board.solution[1].append(move)


    def is_visited(self, board):
        """check if the board has already been visited else add it to the visitied boards"""
        board_as_tuple = tuple(map(tuple, board.show()))
        visited = board_as_tuple in self.visited_boards
        if not visited:
            # add the board as a visited board
            self.visited_boards.add(board_as_tuple)
        return visited

    def create_branch(self, board, car, move):
        """create a new board for a given move"""
        current_board = copy.deepcopy(board)
        current_board.move(current_board.cars[car], move)
        return current_board


    def prune(self, active_boards):
        """sort the active boards and remove all boards where the score is 2 higher then the lowest score"""
        active_boards.sort(key=lambda x: x.score, reverse=False)
        lowest_score = active_boards[0].score
        return [x for x in active_boards if x.score < lowest_score + 2]


    def estimate(self, board):
        """returns the amount of cars in path of the red car"""

        red_car = board.cars['X']
        score = 0

        # check each tile in front of the red car
        for x in board.grid[red_car.row, red_car.col + red_car.length: board.dimension]:
            if x != '_':
                score += 1
        return score
