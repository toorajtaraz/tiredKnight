import chess
import ai
class ChessGame:
    white_player = None
    black_player = None
    board = None

    def __init__(self, w, b, init_state):
        self.white_player = w
        self.black_player = b
        self.board = chess.Board(init_state)

    def play(self):
        print('Initial board:')
        print(ai.unicode_board(self.board))
        print('game begings...')
        while True:
            move = self.white_player.move(self.board)

            self.board.push(move)
            print(ai.unicode_board(self.board))
            if self.board.is_game_over():
                return self.board.outcome()
        
            move = self.black_player.move(self.board)

            self.board.push(move)
            print(ai.unicode_board(self.board))
            if self.board.is_game_over():
                return self.board.outcome()


