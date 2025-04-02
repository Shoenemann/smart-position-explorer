"""Some functionalities inherited from the library 'chess' (see the docs)"""
import chess
import chess.pgn
import io

def pgn_to_fen(pgn: str):
    """
    convert pgn to fen notation
    e.g. 
    pgn = 1. e4
    fen = """
    pgnTextIO = io.StringIO(pgn)
    game = chess.pgn.read_game(pgnTextIO)
    board = game.end().board()
    return board.fen()