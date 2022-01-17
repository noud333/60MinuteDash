from logging import currentframe
from car import Car
import csv
from random import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

'''
For the initialisation of the board, a check needs to be implemented to see if cars do not overlap
Currently this is not necessary as we start with valid boards. But when we generate our own we will need this.
'''


class Board():
    '''
    This class loads the board of the rush hour game
    it inputs the board size (which is n x n) and the name of the csv file with the initial conditions
    '''
    def __init__(self, size, csv_file) -> None:

        # initialising the playing board
        self._board = []
        for i in range(size):
            self._board.append([])
            for j in range(size):
                self._board[i].append(0)

        self._size = size

        # dict with all the cars
        self._cars = dict()

        # dict shifting letters to numbers for the cars
        self._car_number = dict()

        # put the cars on the board
        self.board_load(csv_file)

        # list to save correct moves
        self._moves = []

    def board_load(self, csv_file):
        """ fill the empty board with the cars from csv file """
        with open(csv_file, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            car_counter = 1
            for line in csv_reader:
                # create car objects and save them
                self._cars[car_counter] = Car(line[0], int(line[4]), line[1], int(line[2])-1, int(line[3])-1)
                self._car_number[self._cars[car_counter]._name] = car_counter

                # put cars on board
                for i in range(self._cars[car_counter]._length):
                    x = int(line[2]) - 1
                    y = int(line[3]) - 1

                    # make sure the rest of the car faces the right direction
                    if self._cars[car_counter]._direction == 'H':
                        x += i
                    else:
                        y += i

                    # give it its dict value
                    # ints are used instead of the letters to make randomisation easier
                    self._board[y][x] = car_counter

                car_counter += 1

    def move_car(self, car, movement):
        ''' this function is used to move a car it checks '''

        # check if a valid car has been inputted
        if car in self._cars.keys():
            movable_car = car
        elif car.upper() in self._car_number:
            movable_car = self._car_number[car.upper()]
        else:
            return "Car not found"

        # get the instance of that car
        current_car = self._cars[movable_car]
        empty_slots = 0
        x_pos, y_pos = current_car.get_pos()
        
        # get a stepsize of 1 with the correct sign
        step = int(movement / abs(movement))

        try:
            if current_car._direction == "H":

                # check if there are enough empty slots to complete the move
                while empty_slots < abs(movement):
                    x_pos += step

                    # keep car in bounds
                    if x_pos < 0:
                        return "Invalid Move"

                    # ignore slots that are part of the car
                    if self._board[y_pos][x_pos] == movable_car:
                        pass
                    elif self._board[y_pos][x_pos] == 0:
                        empty_slots += 1
                    else:
                        return "Invalid Move"
            else:

                # check if there are enough empty slots to complete the move
                while empty_slots < abs(movement):
                    y_pos += step

                    # keep car in bounds
                    if y_pos < 0:
                        return "Invalid Move"

                    # skip over the car itself
                    if self._board[y_pos][x_pos] == movable_car:
                        pass
                    elif self._board[y_pos][x_pos] == 0:
                        empty_slots += 1
                    else:
                        return "Invalid Move"
        except IndexError:
            return "Invalid move"

        self.move(movable_car, movement)
        return "Move Completed"

    def move(self, car, movement):
        '''only to be used in other funcitons moves the car itself'''
        current_car = self._cars[car]

        self._moves.append([current_car._name, movement])

        # remove car from board
        for i in range(current_car._length):
            x, y = current_car.get_pos()

            # make sure the rest of the car faces the right direction
            if current_car._direction == 'H':
                x += i
            else:
                y += i

            # remove current car from board
            self._board[y][x] = 0

        x_pos, y_pos = current_car.get_pos()

        if current_car._direction == "H":
            x_pos += movement

        else:
            y_pos += movement

        current_car.update_pos(x_pos, y_pos)

        # put cars on board
        for i in range(current_car._length):
            x = x_pos
            y = y_pos

            # make sure the rest of the car faces the right direction
            if current_car._direction == 'H':
                x += i
            else:
                y += i

            # give it its dict value
            # ints are used instead of the letters to make randomisation easier
            self._board[y][x] = car

    def random_move(self):

        if random() > 0.5:
            step = 1
        else:
            step = -1

        while True:
            number = int(random() * (len(self._car_number)) + 0.5)

            if number in self._cars.keys():
                self.move_car(number, step)
                break

    def victory(self):
        '''Check if red car is at end point'''

        red_car = self._car_number["X"]

        if self._cars[red_car]._xpos == len(self._board) - 2:
            return True

    def print_board(self):
        '''print the board with letters instead of numbers to make it clearer'''

        # create the board made of strings
        pretty_board = []
        for row in range(len(self._board)):
            pretty_board.append([])

            for item in self._board[row]:

                if item == 0:
                    pretty_board[row].append(" ")
                else:
                    pretty_board[row].append(self._cars[item]._name)

        # print the string board
        for line in pretty_board:
            print(line)

    def generate_frame(self):
        '''
        generates a pyplot frame with of the board with the cars

        info about rectangles from: https://www.youtube.com/watch?v=CRMtqTeH2HQ 
        '''
        fig = plt.figure(figsize= (6,6))

        for car in self._cars:
            current_car = self._cars[car]
            x, y = current_car.get_pos()
            
            y = (y * (-1)) - 1
            name, size, dir = current_car.get_val()

            if dir == "H":
                x_size = size
                y_size = 1
            else:
                x_size = 1
                y_size = size
                y = y - size + 1

            if name == "X":
                rec = Rectangle((x,y), x_size, y_size, color="red")
            elif size == 3:
                rec = Rectangle((x,y), x_size, y_size, color= "yellow")
            else:
                rec = Rectangle((x,y), x_size, y_size)

            rec2 = Rectangle((x,y), x_size, y_size, fill=False, color="black")
            plt.gca().add_patch(rec)
            plt.gca().add_patch(rec2)

        plt.xlim(0, self._size)
        plt.ylim(-self._size, 0)
        plt.savefig("test.png")

    def save_output(self, name= "output.csv"):
        '''this function saves the made moves into a csv file'''

        header = ["car", "move"]

        with open(name, "w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)
            csv_writer.writerows(self._moves)
