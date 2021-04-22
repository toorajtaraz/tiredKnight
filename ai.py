from chess import Board
import chess

# based on:
# https://www.chessprogramming.org/Simplified_Evaluation_Function

piece_value = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

pawn_position_based_eval_for_white = [
    0, 0, 0, 0, 0, 0, 0, 0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5, 5, 10, 25, 25, 10, 5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, -5, -10, 0, 0, -10, -5, 5,
    5, 10, 10, -20, -20, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0,
]
pawn_position_based_eval_for_black = list(reversed(pawn_position_based_eval_for_white))

knight_position_based_eval_for_white = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]
knight_position_based_eval_for_black = list(reversed(knight_position_based_eval_for_white))

bishop_position_based_eval_for_white = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
]
bishop_position_based_eval_for_black = list(reversed(bishop_position_based_eval_for_white))

rook_position_based_eval_for_white = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, 10, 10, 10, 10, 5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 5, 5, 0, 0, 0,
]
rook_position_based_eval_for_black = list(reversed(rook_position_based_eval_for_white))

queen_position_based_eval_for_white = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20,
]
queen_position_based_eval_for_black = list(reversed(queen_position_based_eval_for_white))

king_position_based_eval_for_white = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, 20, 0, 0, 0, 0, 20, 20,
    20, 30, 10, 0, 0, 10, 30, 20,
]
king_position_based_eval_for_black = list(reversed(king_position_based_eval_for_white))

king_position_based_eval_for_white_end_game = [
    -50, -40, -30, -20, -20, -30, -40, -50,
    -30, -20, -10,  0,  0, -10, -20, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -30,  0,  0,  0,  0, -30, -30,
    -50, -30, -30, -30, -30, -30, -30, -50
]
king_position_based_eval_for_black_end_game = list(reversed(king_position_based_eval_for_white_end_game))


def evaluate_position(piece: chess.Piece, square: chess.Square, end_game: bool) -> int:
    piece_type = piece.piece_type
    positions = None
    if piece_type == chess.PAWN:
        if piece.color == chess.WHITE:
            positions = pawn_position_based_eval_for_white 
        else:
            positions = pawn_position_based_eval_for_black
    if piece_type == chess.KNIGHT:
        if piece.color == chess.WHITE:
            positions = knight_position_based_eval_for_white 
        else:
            positions = knight_position_based_eval_for_white
    if piece_type == chess.BISHOP:
        if piece.color == chess.WHITE:
            positions = bishop_position_based_eval_for_white 
        else:
            positions = bishop_position_based_eval_for_black
    if piece_type == chess.ROOK:
        if piece.color == chess.WHITE:
            positions = rook_position_based_eval_for_white 
        else:
            positions = rook_position_based_eval_for_black
    if piece_type == chess.QUEEN:
        if piece.color == chess.WHITE:
            positions = queen_position_based_eval_for_white 
        else:
            positions = queen_position_based_eval_for_white
    if piece_type == chess.KING:
        if end_game:
            if piece.color == chess.WHITE:
                positions = king_position_based_eval_for_white_end_game 
            else:
                positions = king_position_based_eval_for_black_end_game

        else:
            if piece.color == chess.WHITE:
                positions = king_position_based_eval_for_white 
            else:
                positions = king_position_based_eval_for_black

    return positions[square]

def are_we_in_end_game(board):
    queens = 0
    bishops_knights = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            if piece.piece_type == chess.QUEEN:
                queens += 1
            if piece.piece_type == chess.KNIGHT or piece.piece_type == chess.BISHOP:
                bishops_knights += 1
    #no one has a queen or no other pieces are on the board
    if queens == 0 or (queens == 2 and bishops_knights <= 1):
        return True
    else:
        return False

def unicode_board(board):
    out = ''
    count = 0
    for square in chess.SQUARES:
        count += 1
        piece = board.piece_at(square)
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

def vanilla_eval(board):
    return 0

def maximizer(board, depth, evaluate=vanilla_eval):
    if board.is_checkmate():
        return -float("inf")
    if depth == 0 or board.is_game_over():
        return evaluate(board)
    value = -float('inf')
    for move in board.legal_moves:
        board.push(move)
        value = max(value, minimizer(board, depth - 1, evaluate))
        board.pop()
    return value

def minimizer(board, depth, evaluate=vanilla_eval):
    if board.is_checkmate():
        return float("inf")
    if depth == 0 or board.is_game_over():
        return evaluate(board)
    value = float('inf')
    for move in board.legal_moves:
        board.push(move)
        value = min(value, maximizer(board, depth - 1, evaluate))
        board.pop()
    return value
