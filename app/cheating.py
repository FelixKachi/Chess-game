from stockfish import Stockfish

class CheatingDetector:
    def __init__(self, stockfish_path):
        self.stockfish = Stockfish(stockfish_path, depth=15)

    def analyze_moves(self, moves):
        self.stockfish.set_position([])
        matches = 0

        for move in moves:
            self.stockfish.set_position(moves[:moves.index(move)])
            best_move = self.stockfish.get_best_move()
            if move == best_move:
                matches += 1

        match_percentage = (matches / len(moves)) * 100
        return match_percentage
