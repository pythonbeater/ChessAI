'''
Responsible for squares' accessibility, to get current state and update it
'''

class Square: 

    def __init__(self, col, row, piece=None) -> None:
        self.col = col
        self.row = row
        self.piece = piece

    def __eq__(self, other: object) -> bool:
        return self.col == other.col and self.row == other.row

    def square_state(self, check_type='piece') -> bool:
        '''
        Check if square has piece
        '''
        if check_type == 'empty':
            return not self.piece != None
        return self.piece != None
    
    def square_piece(self, color, p_type='enemy'): 
        ''' 
        Check if square has rival or team piece
        '''
        if p_type == 'teammate':
            return self.square_state() and self.piece.color == color
        return self.square_state(check_type='piece') and self.piece.color != color

    def empty_or_foe(self, color): 
        '''
        Check if square is empty or has a rival piece
        '''
        return self.square_state(check_type='empty') or self.square_piece(color, p_type='enemy')
    
    # allows to run method without creating an instance
    @staticmethod
    def in_board_range(*args) -> bool: # recieve as many params as it need
        '''
        Checks if move is within board range
        '''
        for arg in args:
            if arg < 0 or arg > 7: 
                return False
        return True
    

