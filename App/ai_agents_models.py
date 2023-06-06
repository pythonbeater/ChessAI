import random

def FindRandomMove(ValidMoves):
    '''
    Return a random movement
    '''
    return ValidMoves[random.randint(0, len(ValidMoves)-1)]
