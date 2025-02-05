import chess
import chess.pgn

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.moves = []

    def make_move(self, move):
        try:
            self.board.push_uci(move)
            self.moves.append(move)
            return True, str(self.board)
        except ValueError:
            return False, "Invalid move."

    def save_pgn(self, filename="game.pgn"):
        game = chess.pgn.Game()
        node = game
        for move in self.moves:
            node = node.add_variation(chess.Move.from_uci(move))
        with open(filename, "w") as file:
            file.write(str(game))
