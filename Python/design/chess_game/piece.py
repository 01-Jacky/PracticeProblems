class Piece:
    def __init__(self):
        self.captured = False

class Rook(Piece):
    def __init__(self):
        Piece.__init__()
