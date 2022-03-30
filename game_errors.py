class InvalidMoveException(Exception):
    """Exception raised from the Board Object when
    the player move is invalid:

    -> No piece in starting pos
    -> new_pos not reachable
    -> nothing to capture on new_pos
    """
    def __init__(self, message="Invalid move"):
        self.message = message
