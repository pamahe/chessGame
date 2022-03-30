from game_errors import InvalidMoveException


class Piece:

    def __init__(self, name, color, pos):
        self.name = name
        self.color = color
        self.pos = pos

    @staticmethod
    def display(self):
        print(self.color, self.pos)

    def get_available_pos(self):
        raise NotImplementedError

    def get_path(self, new_pos):
        raise NotImplementedError

    def move(self, new_pos):
        raise NotImplementedError


class Pawn(Piece):

    instances = 0

    def __init__(self, name, color, pos):
        super().__init__(name, color, pos)
        self.symbol = "p"

    def get_available_pos(self):
        available_pos = []
        if self.color == "black":
            # if in starting pos can move 2 cases forward
            if self.pos[1] == "7":
                available_pos.append(f"{self.pos[0]}5")
            available_pos.append(f"{self.pos[0]}{int(self.pos[1]) - 1}")
        if self.color == "white":
            # if in starting pos can move 2 cases forward
            if self.pos[1] == "2":
                available_pos.append(f"{self.pos[0]}4")
            print(self.pos[1])
            available_pos.append(f"{self.pos[0]}{int(self.pos[1]) + 1}")

        return available_pos

    def get_path(self, new_pos):
        # 1 case forward
        if self.color == "white":
            path = [f"{self.pos[0]}{int(self.pos[1]) + 1}"]
            # 2 case forward if starting position
            if self.pos[1] == "2" and new_pos[1] == "4":
                path.append(f"{self.pos[0]}{int(self.pos[1]) + 2}")

        elif self.color == "black":
            path = [f"{self.pos[0]}{int(self.pos[1]) - 1}"]
            if self.pos[1] == "7" and new_pos[1] == "5":
                path.append(f"{self.pos[0]}{int(self.pos[1]) - 2}")

        raise NotImplementedError

    def move(self, new_pos):
        if new_pos in self.get_available_pos():
            self.pos = new_pos
        else:
            raise InvalidMoveException()



class Rook(Piece):

    instances = 0

    def __init__(self, name, color, pos):
        super().__init__(name, color, pos)
        self.symbol = "R"

    def get_available_pos(self):
        column = self.pos[0]
        row = self.pos[1]

        available_pos = []
        for c in 'abcdefgh':
            available_pos.append(f"{c}{row}")
        for r in '12345678':
            available_pos.append(f"{column}{r}")

        return available_pos

    def get_path(self, new_pos):
        pass

    def move(self, new_pos):
        pass


class Knight(Piece):

    instances = 0

    def __init__(self, name, color, pos):
        super().__init__(name, color, pos)
        self.symbol = "N"

    def get_available_pos(self):
        raise NotImplementedError


class Bishop(Piece):

    instances = 0

    def __init__(self, name, color, pos):
        super().__init__(name, color, pos)
        self.symbol = "B"

    def get_available_pos(self):
        raise NotImplementedError


class Queen(Piece):

    instances = 0

    def __init__(self, name, color, pos):
        super().__init__(name, color, pos)
        self.symbol = "Q"

    def get_available_pos(self):
        raise NotImplementedError


class King(Piece):

    instances = 0

    def __init__(self, name, color, pos):
        super().__init__(name, color, pos)
        self.symbol = "K"

    def get_available_pos(self):
        raise NotImplementedError
