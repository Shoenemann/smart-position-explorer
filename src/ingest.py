from . import chess_functions
import pandas as pd

def my_repertoire_filename():
    return "../data/Opening25 - white.csv"

def my_repertoire_pgns():
    csv_filename = my_repertoire_filename()
    df = pd.read_csv(csv_filename)
    num_rows = df.shape[0]
    repertoire = []
    for i in range(num_rows):
        list_moves = df.iloc[i,4:]
        pgn = chess_functions.list_to_pgn(list_moves)
        repertoire.append(pgn)
    return repertoire

