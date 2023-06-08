import random
from utils import B_DIMENSION
from move_piece import Place
from pieces import *


knight = Knight('black')
knight_value = knight.importance_value

queen = Queen('black')
queen_value = queen.importance_value

bishop = Bishop('black')
bishop_value = bishop.importance_value

rook = Rook('black')
rook_value = rook.importance_value

pawn = Pawn('black')
pawn_value = pawn.importance_value

king = King('black')
king_value = king.importance_value

CHECKMATE = 1000
STALEMATE = 0
PieceImportance = {
                            'knight': knight_value,
                            'queen': queen_value,
                            'bishop': bishop_value,
                            'rook': rook_value,
                            'pawn': pawn_value,
                            'king': king_value
                        } 

# Get the max score in each square
MaxScore = CHECKMATE

class RandomAgent:
    def __init__(self, color):
        self.color = color

    def make_move(self, board):
        # Iterate over all the squares on the board
        for row in range(B_DIMENSION):
            for col in range(B_DIMENSION):
                square = board.squares[col][row]
                # Check if the square has a piece
                if square.piece is not None:
                    piece = square.piece

                    # Check if the piece matches the agent's color
                    if piece.color == 'black':
                        # Calculate all valid moves for the piece
                        board.check_moves(piece, col, row)

                        # Get the list of valid moves for the piece
                        possible_moves = piece.valid_moves

                        if possible_moves:
                            # Select a random move from the list of possible moves
                            random_move = random.choice(possible_moves)

                            # Make the selected move on the board
                            place = Place(random_move.initial, random_move.final)
                            board.move(piece, place)

                            return

        # No possible moves for the agent, so it can't make a move
        print("No possible moves for the agent.")
        
        
        
class BestMovementAgent:

    def __init__(self, color):
        self.color = color
        
        
    def make_move(self, board): 
        pass
        
        
    def MaterialScore(self, piece ,move):
        score = 0
        # Iterate over all the squares on the board
        for row in range(B_DIMENSION):
            for col in range(B_DIMENSION):
                square = board.squares[col][row]
                # Check if the square has a piece
                if square.piece is not None:
                    piece = square.piece

                    # Check if the piece matches the agent's color
                    if piece.color == 'white':
                        if piece.name == 'King':
                            score + King('white').importance_value
                        elif piece.name == 'Queen':
                            score + Queen('white').importance_value 
                        elif piece.name == 'Knight':
                            score + Knight('white').importance_value 
                        elif piece.name == 'Bishop':
                            score + Bishop('white').importance_value 
                        elif piece.name == 'Rook':
                            score + Rook('white').importance_value 
                        elif piece.name == 'Pawn':
                            score + Pawn('white').importance_value 
                    
                elif square.piece is None:
                    score + 0
                    


# class BestMovementAgent:

#     def __init__(self, color):
#         self.color = color

#     def make_move(self, board): 
#         valid_moves = []  # List to store all valid moves

#         # Iterate over all the squares on the board
#         for row in range(B_DIMENSION):
#             for col in range(B_DIMENSION):
#                 square = board.squares[col][row]
#                 # Check if the square has a piece
#                 if square.piece is not None:
#                     piece = square.piece

#                     # Check if the piece matches the agent's color
#                     if piece.color == self.color:
#                         # Calculate all valid moves for the piece
#                         board.check_moves(piece, col, row)

#                         # Get the list of valid moves for the piece
#                         possible_moves = piece.valid_moves

#                         if possible_moves:
#                             valid_moves.extend([(piece, move) for move in possible_moves])  # Append valid moves to the list

#         if valid_moves:
#             # Sort valid moves by score in descending order
#             valid_moves.sort(key=lambda move: self.get_move_score(move[0], move[1]), reverse=True)

#             # Select the move with the highest score
#             piece, best_move = valid_moves[0]

#             # Make the selected move on the board
#             initial_square = board.squares[best_move.initial.col][best_move.initial.row]
#             final_square = board.squares[best_move.final.col][best_move.final.row]
#             captured_piece = final_square.piece  # Check if the move results in capturing an opponent's piece
#             print(captured_piece)
#             place = Place(initial_square, final_square)
#             board.move(piece, place)

#         else:
#             # No possible moves for the agent, so it can't make a move
#             print("No possible moves for the agent.")

#     def get_move_score(self, piece, move):
#         # Calculate the score for a given piece and move
#         initial_score = PieceImportance[piece.name]
#         final_score = 0

#         # Check if the move results in capturing an opponent's piece
#         if move.captured_piece:
#             final_score = PieceImportance[move.captured_piece.name]
#             print(final_score)
#         # Calculate the total score by subtracting the opponent's piece value from the agent's piece value
#         score = initial_score - final_score
#         return score
                    