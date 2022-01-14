"""
This function runs the rush hour game via the board class
"""
import time
from board import Board

class Game():
    def __init__(self, size, name):
        self.size = size
        self.name = name
    
    def random_moves(self):
        begin = time.time()
        test = Board(self.size, self.name)
        test.print_board()

        while True:
            test.random_move()

            if test.victory():
                print("Congrats")
                test.save_output()
                test.print_board()
                test.generate_frame()
                end = time.time()
                print(end - begin)
                break

    def user_played(self):
        begin = time.time()
        test = Board(self.size, self.name)
        test.print_board()

        while True:

            move = input("Next move: ").split()

            print(test.move_car(move[0], int(move[1])))
            test.print_board()

            if test.victory():
                print("Congrats")
                test.save_output()
                test.print_board()
                test.generate_frame()
                end = time.time()
                print(end - begin)
                break

game = Game(6, "Rushhour6x6_1.csv")
game.random_moves()