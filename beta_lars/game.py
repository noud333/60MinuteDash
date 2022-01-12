"""
Contains the Game class that is used to play a game of Rush Hour
"""

from board import Board
import os
import random
import csv

class Game():
    """ Contains all the information needed to play a game of Rush Hour """

    def __init__(self, n, board_file):
        self.board = Board(n)
        self.board.fill_board(board_file)
    
    def solve_random(self):
        """ Will move a random car in a random direction until the board is solved """

        name_list = []
        for car in self.board.cars.keys():
            name_list.append(car)
        total = len(name_list)

        steplist = []

        # make a random move until solved
        while not self.board.is_finished():
            r = random.randrange(0, total)
            car_name = name_list[r]
            direction = random.choice([-1, 1])

            # if the move is valid, save it
            if self.board.move(car_name, direction):
                steplist.append([car_name, direction])
                    
        return steplist

    def save_output(self, steps, output_file_name):
        """ Save the steps in an output file """

        with open(f"files/output/{output_file_name}.csv", "w", newline="") as file:
            writer = csv.writer(file)

            # first the header
            writer.writerow(["car", "move"])
            writer.writerows(steps)

    def play_game(self):
        """ The main game loop """
        
        # continue until finished
        self.board.show_board()
        while not self.board.is_finished():
            
            # ask for a new move
            new_move = input("Car steps: ").split(" ")
            if "quit" in new_move:
                break
            
            # print the current state to the screen
            os.system('cls||clear')
            if not self.board.move(new_move[0], int(new_move[1])):
                print("Invalid move")
            if self.board.is_finished():
                print("Completed!")
            self.board.show_board()
    