class Car():
    '''
    The car class save the size and direction of movement of individual cars.
    '''
    def __init__(self, name, length, direction, x_pos, y_pos):
        self._name = name
        self._length = length
        self._direction = direction
        self._xpos = int(x_pos)
        self._ypos = int(y_pos)

    def update_pos(self, x_pos, y_pos):
        self._xpos = int(x_pos)
        self._ypos = int(y_pos)

    def get_pos(self):
        return self._xpos, self._ypos

    def get_val(self):
        return self._name, self._length, self._direction