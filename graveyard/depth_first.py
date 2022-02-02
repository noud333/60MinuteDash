import copy
import random

class Depth_search():

    def __init__(self, board, depth):
        self.stack = [board]

        self.boards_visited = set()

        self.boards_visited.add(tuple(map(tuple, board.show())))

        self.boards_checked = 0

        self.depth = depth

    def run(self):
        while len(self.stack):

            board = self.stack.pop()

            if len(board.solution[0]) < self.depth:

                moves = board.get_moves()
                moves_indices = range(len(moves[0]))
                #random.shuffle(list(moves_indices))
                

                if self.boards_checked % 1000 <= 5:
                    print(f"Boards Checked {self.boards_checked}")

                for move_index in moves_indices:

                    current_board = copy.deepcopy(board)

                    current_board.move(current_board.cars[moves[0][move_index]], moves[1][move_index])
                    self.boards_checked += 1

                    board_as_tuple = tuple(map(tuple, current_board.show()))

                    if board_as_tuple not in self.boards_visited:
                        
                        current_board.solution[0].append(moves[0][move_index])
                        current_board.solution[1].append(moves[1][move_index])

                        if current_board.finished():
                            return current_board.solution, current_board, self.boards_checked

                        self.boards_visited.add(board_as_tuple)
                        self.stack.append(current_board)
