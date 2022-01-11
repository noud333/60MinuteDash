from car import Car
import csv
from random import random

class board():
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
        
        self._cars = dict()
        self._car_number = dict()

        self.board_load(csv_file)
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
        x_pos = current_car._xpos
        y_pos = current_car._ypos
        step = int(movement / abs(movement))
        
        try:
            if current_car._direction == "H":
                while empty_slots < abs(movement):
                    x_pos += step

                    if x_pos < 0:
                        return "Invalid Move"

                    if self._board[y_pos][x_pos] == movable_car:
                        pass
                    elif self._board[y_pos][x_pos] == 0:
                        empty_slots += 1
                    else:
                        return "Invalid Move"
            else:
                while empty_slots < abs(movement):
                    y_pos += step

                    if y_pos < 0:
                        return "Invalid Move"
                
                    if self._board[y_pos][x_pos] == movable_car:
                        pass
                    elif self._board[y_pos][x_pos] == 0:
                        empty_slots += 1
                    else:
                        return "Invalid Move"
        except:
            return "Invalid move"

        self.move(movable_car, movement)
        return "Move Completed"

    def move(self, car, movement):
        '''only to be used in other funcitons moves the car itself'''
        current_car = self._cars[car]

        self._moves.append([current_car._name, movement])

        # remove car from board
        for i in range(current_car._length):
            x = current_car._xpos
            y = current_car._ypos
            
            # make sure the rest of the car faces the right direction
            if current_car._direction == 'H':
                x += i
            else:
                y += i

            # remove current car from board
            self._board[y][x] = 0

        x_pos = current_car._xpos
        y_pos = current_car._ypos

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

    def victory(self):
        '''Check if red car is at end point'''

        red_car = self._car_number["X"]

        if self._cars[red_car]._xpos == len(self._board) -2:
            return True
    
    def save_output(self):
        '''this function saves the made moves into a csv file'''

        header = ["car", "move"]

        with open("output.csv", "w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)
            csv_writer.writerows(self._moves)
    
    def random_move(self):      
        
        if random() > 0.5:
            step = 1
        else:
            step = -1
        
        while True:
            number = int(random() * (len(self._car_number )) + 0.5)

            if number in self._cars.keys():
                self.move_car(number, step)
                break
        

test = board(6, "Rushhour6x6_3.csv")
test.print_board()

while True:
    
    #move = input("Next move: ").split()

    #print(test.move_car(move[0], int(move[1])))
    #test.print_board()
    test.random_move()

    if test.victory():
        print("Congrats")
        test.save_output()
        break