"""
Contains the Car class for a Rush Hour game
"""

class Car():
    """ A Car with a name, its orientation, its location and its length """

    def __init__(self, name, orientation, col, row, length):
        self.name = name
        self.is_horizontal = orientation == "H"
        self.col = col
        self.row = row
        self.length = length
    
    def __str__(self):
        return f"{self.name} at ({self.row}, {self.col})"

    def get_location(self):
        """ Gives the current (row, col) location """
        return self.row, self.col
    
    def get_name(self):
        """ Gives the name of this car """
        return self.name

    def move(self, steps):
        """ Moves the car steps times in its direction """
        if self.is_horizontal:
            self.col += steps
        else:
            self.row += steps