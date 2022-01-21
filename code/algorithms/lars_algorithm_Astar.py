"""
A* with an archive for pruning
Heuristic: steps for red car to finish + cars blocking its path
"""
# liever carnames vanuit get moves!

import copy


class Node():

    def __init__(self, solution_path, board):
        self.solution_path = solution_path
        self.board = board
        self.score = self.get_score()
    
    def get_score(self):
        """ Uses the heuristic for a score """
        score = len(self.solution_path[0])
        red_car = self.board.cars["X"]
        score -= red_car.col * 4
        blocking = len(set(str(self.board.grid[red_car.row, red_car.col + red_car.length:self.board.dimension])))
        # blocking_above = len(set(str(self.board.grid[red_car.row - 1, red_car.col + red_car.length:self.board.dimension])))
        # blocking_under = len(set(str(self.board.grid[red_car.row + 1, red_car.col + red_car.length:self.board.dimension])))
        score += blocking * 2
        return score


class Algorithm():

    def __init__(self, board):
        self.original_board = board
        self.nodes = [Node([[], []], copy.deepcopy(self.original_board))]
        self.uniques = set()

    def run(self):
        """ 
        Perform the algorithm until a solution is found
        """

        while self.nodes:
            solution, board = self.check_node()
            if solution:
                return solution, board 
        
        # in case of an error
        return [[], []], self.original_board
    
    def add_node(self, new_node):
        """
        Uses a node's score to place it in the node list, keep the best ... nodes
        """       
        
        index = 0
        for node in self.nodes:
            if new_node.score < node.score:
                self.nodes.insert(index, new_node)
                break
            index += 1

        if not new_node in self.nodes:
            self.nodes.append(new_node)

        if len(self.nodes) > 500:
            # too big remove last one
            self.nodes.pop()


    def check_node(self):
        """ 
        Check the node with the highest priority/the lowest score
        """

        # get the node
        node = self.nodes.pop(0)

        # make a node for each move
        moves = node.board.get_moves()
        old_path = node.solution_path
        if moves:
            for i in range(len(moves[0])):
                new_board = copy.deepcopy(node.board)

                car_name = moves[0][i].name
                move = moves[1][i]

                # perform the move
                new_board.move(new_board.cars[car_name], move)

                # stop if the board is solved
                if new_board.finished():
                    the_solution = copy.deepcopy(old_path)
                    the_solution[0].append(car_name)
                    the_solution[1].append(move)
                    return the_solution, new_board

                # check if the move is not yet done
                grid = str(new_board.grid)
                if not grid in self.uniques:
                    self.uniques.add(grid)
                    # make new node
                    solution_path = copy.deepcopy(old_path)
                    solution_path[0].append(car_name)
                    solution_path[1].append(move)
                    new_node = Node(solution_path, new_board)
                    self.add_node(new_node)

        return False, False
