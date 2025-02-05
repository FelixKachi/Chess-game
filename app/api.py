from flask import Flask, request, jsonify
from app.game import ChessGame
from app.cheating import CheatingDetector

app = Flask(__name__)

# Initialize game and Stockfish path
chess_game = ChessGame()
detector = CheatingDetector("/path/to/stockfish")

@app.route("/move", methods=["POST"])
def make_move():
    data = request.json
    move = data.get("move")
    valid, board_state = chess_game.make_move(move)
    if valid:
        return jsonify({"status": "success", "board": board_state})
    else:
        return jsonify({"status": "error", "message": "Invalid move."})

@app.route("/analyze", methods=["GET"])
def analyze():
    moves = chess_game.moves
    match_percentage = detector.analyze_moves(moves)
    return jsonify({"match_percentage": match_percentage})
