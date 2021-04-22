from chess import Board, Move, STARTING_FEN
from ChessGame import ChessGame
from MiniMaxPlayer import MiniMaxPlayer
import chess
white_player = MiniMaxPlayer(chess.WHITE, 'cool white')
black_player = MiniMaxPlayer(chess.BLACK, 'cool black')

game = ChessGame(white_player, black_player, STARTING_FEN)

print(game.play())
