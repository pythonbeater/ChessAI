'''
Responsible for squares' accessibility, to get current state and update it
'''

class Square: 

    def __init__(self, col, row, piece=None):
        self.col = col
        self.row = row
        self.piece = piece

    def square_state(self) -> bool: 
        return self.piece != None