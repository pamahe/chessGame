import json
from itertools import cycle

from board import Board
from game_errors import InvalidMoveException


def make_turn(color, board):
    move = input(f"{color}, your move : ")

    # if movement
    if '-' in move:
        board.make_move(color, move)
    # if capture
    elif 'x' in move:
        board.make_capture(color, move)
    else:
        raise InvalidMoveException()


def run():
    board = Board("starting_board.json")
    board.display()

    turn_iterator = cycle(["white", "black"])
    while True:
        try:
            make_turn(next(turn_iterator), board)
        except InvalidMoveException as e:
            print(e.message)
            # That way we skip the next color and go back to the current one in make_turn
            next(turn_iterator)


if __name__ == '__main__':
    run()
