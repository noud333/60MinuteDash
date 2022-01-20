import copy
import numpy as np

class Breadth_search():

    def __init__(self, board):
        self.board = copy.deepcopy(board)
        self.solution = [[],[]]
 
    def run(self):

        visited_boards = set()
        visited_boards.add(tuple(map(tuple, self.board.show())))
        self.board.score = self.estimate(self.board)
        active_boards = [self.board]
        steps = 0

        while True:

            steps +=1
            print(f"Currently looking at step: {steps}")

            if len(active_boards) > 0:
                active_boards.sort(key=lambda x: x.score, reverse=False)
                lowest_score = active_boards[0].score
                active_boards = [x for x in active_boards if x.score < lowest_score + 2]

            boards = active_boards[:]
            active_boards = []

            for board in boards:
                available_moves = board.get_moves()

                for x in range(len(available_moves[0])):
                    current_board = copy.deepcopy(board)
                    current_board.move(current_board.cars[available_moves[0][x].name], available_moves[1][x])

                    board_as_tuple = tuple(map(tuple, current_board.show()))                  
                    if board_as_tuple not in visited_boards:
                        current_board.score = self.estimate(current_board)
                        active_boards.append(current_board)

                        current_board.solution[0].append(available_moves[0][x].name)
                        current_board.solution[1].append(available_moves[1][x])
                        visited_boards.add(board_as_tuple)

                        if current_board.finished():
                            return current_board.solution, current_board

    def estimate(self, board):
        red_car = board.cars['X']
        score = 0
        for x in board.grid[red_car.row, red_car.col + red_car.length: board.dimension]:
            if x != '_':
                score += 1
        return score


