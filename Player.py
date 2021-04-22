class Player:
    player_color = None
    nick_name = None
    def __str__(self):
        return '{} playing as {}'.format(self.nickName, self.playerColor)

    def __init__(self, color, nick):
        self.nick_name = nick
        self.player_color = color

    def move(self, board):
        pass
 
