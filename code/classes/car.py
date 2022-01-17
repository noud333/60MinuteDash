class Car:
    '''
    this class represents each individual car
    the cars can then be added onto the board
    '''
    def __init__(self, name, orientation, col, row, length):
        self.name = name
        self.is_horizontal = orientation == "H"
        self.col = col
        self.row = row
        self.length = length
