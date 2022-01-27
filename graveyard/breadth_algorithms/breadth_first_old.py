import copy


class Breadth_search():
    """
    Breath first algorithm making use of archive to save visited states.
    Makes use of prunning by cutting states with a score of 2 higher than the minimum.
    Due to optimising based on memory use, it may cause the best solution to be missed.
    """
    def __init__(self, board):
        self.board = copy.deepcopy(board)
        self.boards_checked = 0

    def run(self):

        # save the boards that have already been visited
        visited_boards = set()
        visited_boards.add(tuple(map(tuple, self.board.show())))

        # save the starting board in active boards
        self.board.score = self.estimate(self.board)
        active_boards = [self.board]

        # count the number of steps it takes
        steps = 0
        unique_boards = 0

        while True:

            # show the current layer the algorithm is at
            steps += 1
            print(f"Currently looking at step: {steps}")

            # sort the active boards and remove all boards where the score is 2 higher then the lowest score
            # this is the pruning step
            active_boards.sort(key=lambda x: x.score, reverse=False)
            lowest_score = active_boards[0].score
            active_boards = [x for x in active_boards if x.score < lowest_score + 2]

            # make a copy of the active boards
            boards = active_boards[:]
            active_boards = []

            # for every board create branching paths
            for board in boards:

                # get every available move and create a new branch for every move
                available_moves = board.get_moves()
                for x in range(len(available_moves[0])):
                    current_board = copy.deepcopy(board)
                    current_board.move(current_board.cars[available_moves[0][x]], available_moves[1][x])
                    self.boards_checked += 1

                    # check if the board has already been visited
                    board_as_tuple = tuple(map(tuple, current_board.show()))
                    if board_as_tuple not in visited_boards:
                        
                        unique_boards += 1

                        # add the the new board to the boards for the next iteration
                        current_board.score = self.estimate(current_board)
                        active_boards.append(current_board)
                        current_board.solution[0].append(available_moves[0][x])
                        current_board.solution[1].append(available_moves[1][x])

                        # add the board as a visited board
                        visited_boards.add(board_as_tuple)

                        # check if the victory condition has been met
                        if current_board.finished():
                            return current_board.solution, current_board, unique_boards, self.boards_checked

    def estimate(self, board):
        """returns the amount of cars in path of the red car"""

        red_car = board.cars['X']
        score = 0

        # check each tile in front of the red car
        for x in board.grid[red_car.row, red_car.col + red_car.length: board.dimension]:
            if x != '_':
                score += 1
        return score
