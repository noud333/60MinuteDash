import copy

class Optimizer():
    def __init__(self, board, solution):
        self.original_board = copy.deepcopy(board)
        self.solution = copy.deepcopy(solution)
    
    def load(self):
        pass
    
    def run(self):
        # loop door stappen, zoek redudant moves
        
        while self.remove_empty_spots():
            pass
        # self.remove_empty_spots()
        is_valid, board = self.check_validity()
        return self.solution, board, is_valid

    
    def remove_empty_spots(self):
        self.board = copy.deepcopy(self.original_board)
        positions_to_remove = []

        empty_spots = {}
        # haal redudant moves weg
        for x in range(len(self.solution[0])):
            car, move = self.solution[0][x], self.solution[1][x]

            filled, empty = self.move(self.board.cars[car], move)

            # remove empty spot if it already exists (in case a car makes the same move)
            for key in empty_spots.keys():
                if empty_spots[key][0] == car and key != filled:
                    empty_spots.pop(key)
                    break
                
            empty_spots[empty] = (car, x)
            

            try:
                # print(filled, car)
                # print(empty)
                # input(empty_spots)
                if empty_spots[filled][0] == car:

                    # add a redundent move to remove later
                    positions_to_remove.append(empty_spots[filled][1])
                    positions_to_remove.append(x)
                    empty_spots.pop(filled)
                    empty_spots.pop(empty)
                else:
                    empty_spots.pop(filled)    
            except KeyError:
                pass
        
        # add redundant moves at the end
        print(empty_spots)
        for position in empty_spots:
            if empty_spots[position][0] != "X":
                positions_to_remove.append(empty_spots[position][1])
        
        

        #print(positions_to_remove)
        if len(positions_to_remove) > 0:
            positions_to_remove.sort(reverse=True)

            for i in positions_to_remove:
                self.solution[0].pop(i)
                self.solution[1].pop(i)
            
            return True
        else:
            return False

                            
    def move(self, car, move):
        # empty = (row, col)
        if car.is_horizontal:
            # positive move: left empty, right filled
            if move > 0:
                empty = (car.row, car.col)
                filled = (car.row, car.col + car.length)
            else:
                empty = (car.row, car.col + car.length - 1)
                filled = (car.row, car.col - 1)
        else:
            # vertical movement
            if move > 0:
                empty = (car.row, car.col)
                filled = (car.row + car.length, car.col)
            else:
                empty = (car.row + car.length - 1, car.col)
                filled = (car.row - 1, car.col)
        
        # move the car
        self.board.move(car, move)

        return filled, empty
    
    def check_validity(self):
        board = copy.deepcopy(self.original_board)
        is_valid = True

        for i in range(len(self.solution[0])):
            car, move = self.solution[0][i], self.solution[1][i]
            
            if not board.check_move(board.cars[car], move):
                is_valid = False
                print(board.show(), car, move)
            board.move(board.cars[car], move)

        return is_valid, board
        