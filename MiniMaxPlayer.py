import chess
from Player import Player
from ai import *

class MiniMaxPlayer(Player):
    max_depth = 2
    move_count = 0
    def evaluate(self, board: chess.Board) -> float:
        total = 0
        end_game = are_we_in_end_game(board)

        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if not piece:
                continue

            value = piece_value[piece.piece_type] + evaluate_position(piece, square, end_game)
            if piece.color == chess.WHITE:
                total += value
            else:
                total -= value

        return total


    def move(self, board: chess.Board) -> chess.Move:
        value = -float('inf') if self.player_color else float('inf')
        best_move = None
        legal_moves = list(board.legal_moves)
        for move in legal_moves:
            board.push(move)
            if board.is_checkmate():
                board.pop()
                return move
            if board.is_game_over():
                value = max(value, self.evaluate(board)) if self.player_color else min(value, self.evaluate(board))
                if self.player_color:
                    if temp >= value:
                        value = temp
                        best_move = move
                else:
                    if temp <= value:
                        value = temp
                        best_move = move

                board.pop()
                continue
            if board.can_claim_draw():
                temp = 0
            else:
                temp = minimizer(board, self.max_depth, self.evaluate) if self.player_color else maximizer(board, self.max_depth, self.evaluate)
            if self.player_color:
                if temp >= value:
                    value = temp
                    best_move = move
            else:
                if temp <= value:
                    value = temp
                    best_move = move
            board.pop()
        print(value)
        self.move_count += 1
        return best_move

