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

def list_to_pgn(list_moves_str):
    """
    example:  
        input = ["e4", "e5", "Nf3"]
        output = "1. e4 e5 2. Nf3"
    """
    pgn = ""
    for i, move in enumerate(list_moves_str):
        if move is None or move == "" or pd.isna(move):
            break
        if i%2 == 0:
            # it is a white move
            num_move = 1+(i//2)
            pgn += " "
            pgn += str(num_move) 
            pgn += "."
        pgn +=  " " 
        pgn +=  move
        i+=1
    return pgn