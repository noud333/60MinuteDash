import copy

from code.classes.car import Car
#import random


    
class Greedy(): 
    """solves the board with the greedy algorithm"""

    def __init__(self, board):
        self.board = copy.deepcopy(board)
        # save the solution in a list of two lists
        self.solution = [[],[]]
    
    def run(self):
        red_car = self.board.cars["X"]
        
        while not self.board.finished():
            # move red car towards the exit
            self.recursive(red_car)
        
        return self.solution, self.board

    def recursive(self, car, previous_car=None):

        # print the board just for checking (remove later)
        print(self.board.show())
        

        if not car:
            return
        
        print("car :", car.name)
        if previous_car:
            print("previous_car = : ", previous_car.name)

        forward = self.board.check_move(car, 1)
        backward = self.board.check_move(car, -1)
        if forward:
            while self.board.check_move(car, 1):
                self.board.move(car, 1)
                self.solution[0].append(car.name)
                self.solution[1].append(1)
            self.recursive(self.board.get_neighbor(car, True), car)

        elif backward:
            while self.board.check_move(car, -1):
                self.board.move(car, -1)
                self.solution[0].append(car.name)
                self.solution[1].append(-1)
            
            if car is not self.board.cars["X"]:
                self.recursive(self.board.get_neighbor(car, False), car)
            else:
                self.recursive(previous_car, car)
            
        else:
            neighbor = self.board.get_neighbor(car, True)
            if neighbor is previous_car:
                self.recursive(self.board.get_neighbor(car, False), car)
            elif neighbor is None:
                self.recursive(self.board.get_neighbor(car, False), car)
            else:
                self.recursive(self.board.get_neighbor(car, True), car)
            # if neighbor != previous_car:
            #     self.recursive(self.board.get_neighbor(car,True), previous_car=car)
            # elif neighbor == previous_car:
            #     self.recursive(self.board.get_neighbor(car, False), previous_car = car)
            # elif self.board.get_neighbor(car,False) == previous_car:
            #     self.recursive(self.board.get_neighbor(car, False), previous_car=car)
            
            
        

        # move car, else move the blocking car

        # get car blocking this car
        # check if forward moves on that car will unblock
        # else check if backward moves on that car will unblock
        # else re run on that car