class NumberOfGamesContainer(object):
    """description of class"""

    def __init__(self,  username="", game_count=0, win_count=0):

        self.username = username
        self.game_count = game_count
        self.win_count = win_count
        if game_count != 0:
            self.wins_as_percentage_of_games_played = (win_count / game_count) * 100
        else:
            self.wins_as_percentage_of_games_played = 0

