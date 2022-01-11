"""
Contains the Game class that is used to play a game of Rush Hour
"""

from board import Board
import os

class Game():
    """ Contains all the information needed to play a game of Rush Hour """

    def __init__(self, n, board_file):
        self.board = Board(n)
        self.board.fill_board(board_file) 
    
    def run(self):
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
    