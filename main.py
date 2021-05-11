from chess import Board, Move
from ChessGame import ChessGame
from MiniMaxPlayer import MiniMaxPlayer
import chess
white_player = MiniMaxPlayer(chess.WHITE, 'cool white')
black_player = MiniMaxPlayer(chess.BLACK, 'cool black')
FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

while True:
    try:
        print('0.standard\n1.sixteen pawns\n2.weak!\n3.charge of the light brigade\n')
        num = int(input('your choice: '))
        if num == 0:
            break
        elif num == 1:
            FEN = 'rnbqkbnr/pppppppp/8/8/1PP2PP1/1PP2PP1/PPPPPPPP/RNB1KBNR w KQkq - 0 1'
        elif num == 2:
            FEN = 'nnnnknnn/pppppppp/2p2p2/1pppppp1/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        elif num == 3:
            FEN = 'nnnnknnn/pppppppp/8/8/8/8/PPPPPPPP/1Q1QK1Q1 w KQkq - 0 1'
        else:
            raise(Exception)
        break
    except Exception:
        print('your choice must be a number in range [0..3]')
        continue

game = ChessGame(white_player, black_player, FEN)

print(game.play())
