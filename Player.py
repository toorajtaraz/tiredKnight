import chess

class Player:
    player_color = chess.WHITE
    nick_name = 'generic player'
    def __str__(self):
        return '{} playing as {}'.format(self.nickName, self.playerColor)

    def __init__(self, color: bool, nick: str):
        self.nick_name = nick
        self.player_color = color

    def move(self, board: chess.Board) -> chess.Move:
        pass
 
