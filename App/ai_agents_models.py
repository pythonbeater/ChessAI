import random
from utils import B_DIMENSION
from move_piece import Place

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
