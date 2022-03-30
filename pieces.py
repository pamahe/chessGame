class Piece:

    def __init__(self, name, color, pos):
        self.name = name
        self.color = color
        self.pos = pos

    @staticmethod
    def display(self):
        print(self.color, self.pos)


class Pawn(Piece):

    instances = 0

    def __init__(self, name, color, pos):
        super().__init__(name, color, pos)
        self.symbol = "p"
        Pawn.instances += 1

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
            available_pos.append(f"{self.pos[0]}{int(self.pos[1]) + 1}")

        return available_pos

    def move(self, new_pos):
        if new_pos in self.get_available_pos():
            self.pos = new_pos


class Rook(Piece):

    instances = 0

    def __init__(self, name, color, pos):
        super().__init__(name, color, pos)
        self.symbol = "R"
        Pawn.instances += 1


class Knight(Piece):

    instances = 0

    def __init__(self, name, color, pos):
        super().__init__(name, color, pos)
        self.symbol = "N"
        Pawn.instances += 1


class Bishop(Piece):

    instances = 0

    def __init__(self, name, color, pos):
        super().__init__(name, color, pos)
        self.symbol = "B"
        Pawn.instances += 1


class Queen(Piece):

    instances = 0

    def __init__(self, name, color, pos):
        super().__init__(name, color, pos)
        self.symbol = "Q"
        Pawn.instances += 1


class King(Piece):

    instances = 0

    def __init__(self, name, color, pos):
        super().__init__(name, color, pos)
        self.symbol = "K"
        Pawn.instances += 1
