import random
from utils import B_DIMENSION
from move_piece import Place

class RandomAgent:
    def __init__(self, color):
        self.color = color

    def make_move(self, board):
        # Create a list to store all the pieces with valid moves
        pieces_with_moves = []

        # Iterate over all the squares on the board
        for row in range(B_DIMENSION):
            for col in range(B_DIMENSION):
                square = board.squares[col][row]

                # Check if the square has a piece
                if square.piece is not None:
                    piece = square.piece

                    # Check if the piece matches the agent's color
                    if piece.color == self.color:
                        # Calculate all valid moves for the piece
                        board.check_moves(piece, col, row)

                        # Check if the piece has valid moves
                        if piece.valid_moves:
                            # Add the piece to the list of pieces with valid moves
                            pieces_with_moves.append(piece)

        if pieces_with_moves:
            # Select a random piece from the list of pieces with valid moves
            random_piece = random.choice(pieces_with_moves)

            # Get the list of valid moves for the selected piece
            possible_moves = random_piece.valid_moves

            # Select a random move from the list of possible moves
            random_move = random.choice(possible_moves)

            # Make the selected move on the board
            place = Place(random_move.initial, random_move.final)
            board.move(random_piece, place)
        else:
            # No possible moves for the agent, so it can't make a move
            print("No possible moves for the agent.")
