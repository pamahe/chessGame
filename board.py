import json

from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from game_errors import InvalidMoveException


class Board:

    def __init__(self, filename):
        self.filename = filename
        self.pieces = self.parse_board_file()
        # Board object is current state + history
        # So we keep captured_pieces and moves
        self.captured_pieces = {"white": [], "black": []}
        self.moves = {"white": [], "black": []}

    def parse_board_file(self):
        with open(self.filename, "r") as file:
            s = json.load(file)

        pieces = []
        for obj in s:
            if obj['name'][1] == "P":
                piece = Pawn(obj["name"], obj["color"], obj["pos"])
                pieces.append(piece)
            elif obj['name'][1] == "R":
                piece = Rook(obj["name"], obj["color"], obj["pos"])
                pieces.append(piece)
            elif obj['name'][1] == "B":
                piece = Bishop(obj["name"], obj["color"], obj["pos"])
                pieces.append(piece)
            elif obj['name'][1] == "N":
                piece = Knight(obj["name"], obj["color"], obj["pos"])
                pieces.append(piece)
            elif obj['name'][1] == "Q":
                piece = Queen(obj["name"], obj["color"], obj["pos"])
                pieces.append(piece)
            elif obj['name'][1] == "K":
                piece = King(obj["name"], obj["color"], obj["pos"])
                pieces.append(piece)
        return pieces

    def get_piece(self, position):
        for piece in self.pieces:
            if piece.pos == position:
                return piece
        return None

    def get_pieces_position(self):
        pieces_positions = []
        for piece in self.pieces:
            pieces_positions.append(piece.pos)
        return pieces_positions

    def transform_pawn(self, color, pos):
        new_piece = ""
        while new_piece == "":
            new_piece = input(f"Transform you pawn at {pos} into : ")
            for index, piece in enumerate(self.pieces):
                # Piece is already moved, we only need to delete it
                if piece.pos == pos:
                    del self.pieces[index]

            if new_piece.upper() == "ROOK" or new_piece.upper() == "R":
                piece = Rook(f"{color[0]}RT", color, pos)
                self.pieces.append(piece)
            elif new_piece.upper() == "KNIGHT" or new_piece.upper() == "N":
                piece = Knight(f"{color[0]}NT", color, pos)
                self.pieces.append(piece)
            elif new_piece.upper() == "BISHOP" or new_piece.upper() == "B":
                piece = Bishop(f"{color[0]}BT", color, pos)
                self.pieces.append(piece)
            elif new_piece.upper() == "QUEEN" or new_piece.upper() == "Q":
                piece = Queen(f"{color[0]}QT", color, pos)
                self.pieces.append(piece)
            else:
                new_piece = ""

    def make_move(self, color, move):
        pos = move.split('-')[0][1:3]
        new_pos = move.split('-')[1]

        move_done = False
        for index, piece in enumerate(self.pieces):
            if piece.color == color:
                if piece.pos == pos:
                    if new_pos in piece.get_available_pos():

                        # Check if piece on path
                        if piece.symbol != 'N':
                            if any([p in self.get_pieces_position() for p in piece.get_path(new_pos)]):
                                raise InvalidMoveException("Path blocked")

                        print("making the move")
                        self.moves[color].append(move)
                        piece.move(new_pos)

        if not move_done:
            raise InvalidMoveException()

        self.display()

    def make_capture(self, color, move):
        pos = move.split('-')[0][1:3]
        new_pos = move.split('x')[1]

        pawn_transformation = False
        move_done = False
        for index, piece in enumerate(self.pieces):
            if piece.pos == new_pos:
                self.captured_pieces[color].append(piece.symbol)
                del self.pieces[index]
            if piece.pos == pos:
                self.pieces[index].pos = new_pos
                if piece.symbol == 'p':
                    if new_pos[1] == "8" or new_pos[1] == "1":
                        pawn_transformation = True

        if not move_done:
            raise InvalidMoveException()

        self.moves[color].append(move)

        self.display()
        if pawn_transformation:
            self.transform_pawn(color, new_pos)
        self.display()

    def display(self):
        print("\n          black          \n")
        print("     a  b  c  d  e  f  g  h\n")
        for row in range(8, 0, -1):
            board_row = f"{row}    "
            for column in "abcdefgh":
                piece = self.get_piece(f"{column}{row}")
                if piece:
                    board_row += f"{piece.symbol}  "
                else:
                    board_row += "   "
            print(board_row)
        print("\n         white        ")

        print("Captured pieces : ")
        print("White : ", self.captured_pieces["white"])
        print("Black : ", self.captured_pieces["black"], end="\n\n")
