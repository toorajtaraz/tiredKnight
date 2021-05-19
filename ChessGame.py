import chess
import ai
import platform
import os
def clear_screen():
    plt = platform.system()
    if  plt == 'Linux' or plt == 'Darwin':
        os.system('clear')
    elif plt == 'Windows':
        os.system('CLS')

class ChessGame:
    white_player = None
    black_player = None
    board = None

    def __init__(self, w, b, init_state):
        self.white_player = w
        self.black_player = b
        self.board = chess.Board(init_state)
    def __str__(self) -> str:
        out = ''
        count = 0
        for square in chess.SQUARES:
            count += 1
            piece = self.board.piece_at(square)
            if not piece:
                out += "·"
            if piece and piece.color == chess.WHITE:
                if piece.piece_type == chess.PAWN:
                    out += "♟"
                if piece.piece_type == chess.KNIGHT:
                    out += "♞"
                if piece.piece_type == chess.BISHOP:
                    out += "♝"
                if piece.piece_type == chess.ROOK:
                    out += "♜"
                if piece.piece_type == chess.QUEEN:
                    out += "♛"
                if piece.piece_type == chess.KING:
                    out += "♚"
            if piece and piece.color == chess.BLACK:
                if piece.piece_type == chess.PAWN:
                    out += "♙"
                if piece.piece_type == chess.KNIGHT:
                    out += "♘"
                if piece.piece_type == chess.BISHOP:
                    out += "♗"
                if piece.piece_type == chess.ROOK:
                    out += "♖"
                if piece.piece_type == chess.QUEEN:
                    out += "♕"
                if piece.piece_type == chess.KING:
                    out += "♔"
            out += ' '
            if count == 8:
                out += '\n'
                count = 0
        return out
    def play(self) -> chess.Outcome:
        while True:
            move = self.white_player.move(self.board)
            self.board.push(move)
            clear_screen() 
            print(self)
            if self.board.is_game_over():
                return self.board.outcome()
        
            move = self.black_player.move(self.board)
            self.board.push(move)
            clear_screen() 
            print(self)
            if self.board.is_game_over():
                return self.board.outcome()


