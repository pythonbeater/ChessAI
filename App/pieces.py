'''

'''
import os

######### PARENT CLASS #########

class Pieces: 

    def __init__(self, name, color, importance_value, img_url=None, img_rect=None) -> None:
        self.name = name
        self.color = color
        # the AI will calculate pieces importance value in the white pieces perspective
        importance_notion =  1 if color == 'white' else -1
        self.importance_value = importance_value * importance_notion
        self.valid_moves = []
        self.moved = False
        self.img_url = img_url
        self.set_img()
        self.img_rect = img_rect

    def set_img(self, size=80):
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.img_url = os.path.join(current_dir, 'Assets', 'Images', 'Pieces_{}px'.format(size), '{}_{}.png'.format(self.color, self.name.strip()))

    def add_valid_moves(self, move): 
        self.valid_moves.append(move)

    def clear_moves(self): 
        self.valid_moves = []

######### CHILD CLASSES #########

class Pawn(Pieces): 
    def __init__(self, color) -> None:
        super().__init__('pawn', color, 1.)
        # if its color is white it means it'll move upwards
        self.dir  = -1 if color == 'white' else 1 # in pygame the y axis decreaases going up
        # En Passant
        self.en_passant = False
        
class Knight(Pieces): 
    def __init__(self, color) -> None:
        super().__init__('knight', color, 3)
        
class Bishop(Pieces): 
    def __init__(self, color) -> None:
        super().__init__('bishop', color, 3.001)

class Rook(Pieces): 
    def __init__(self, color) -> None:
        super().__init__('rook ', color, 5.)

class Queen(Pieces): 
    def __init__(self, color) -> None:
        super().__init__('queen', color, 10.)

class King(Pieces):
    def __init__(self, color) -> None:
        self.left_rook = None
        self.right_rook = None
        super().__init__('king', color, 9e99)
