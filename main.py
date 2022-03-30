import json
from itertools import cycle

from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from board import Board


def make_turn(color, board):
    move = input(f"{color}, your move : ")

    # if movement
    if '-' in move:
        print("Function make_move")
        board.make_move(color, move)

    # if capture
    if 'x' in move:
        board.make_capture(color, move)
        pass


def run():
    board = Board("starting_board.json")
    board.display()

    turn_iterator = cycle(["white", "black"])
    while True:
        make_turn(next(turn_iterator), board)


if __name__ == '__main__':
    run()
