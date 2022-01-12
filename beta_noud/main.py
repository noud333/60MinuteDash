"""
This function runs the rush hour game via the board class
"""
import time
from board import Board


begin = time.time()
test = Board(6, "Rushhour6x6_1.csv")
test.print_board()

while True:

    # move = input("Next move: ").split()

    # print(test.move_car(move[0], int(move[1])))
    # test.print_board()
    test.random_move()

    if test.victory():
        print("Congrats")
        test.save_output()
        test.print_board()
        test.generate_frame()
        end = time.time()
        print(end - begin)
        break
