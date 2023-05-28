'''
Responsible for getting squares' state
'''

class Square: 

    def __init__(self, col, row, piece=None):
        self.col = col
        self.row = row
        self.piece = piece