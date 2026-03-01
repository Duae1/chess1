class Puzzle:
    def __init__(self, dict_data):
        self.puzzle = dict_data
        self.fen = None
        self.id = None
        self.moves = None
        self.rating_deviation = None
        self.popularity = None
        self.nb_plays = None
        self.themes = None

    def get_Fen(self):
        self.fen = self.puzzle['FEN']

    def get_Id(self):
        self.id = self.puzzle['PuzzleId']

    def get_Moves(self):
        self.moves = self.puzzle['Moves']

    def get_RatingDeviation(self):
        self.rating_deviation = self.puzzle['RatingDeviation']

    def get_Popularity(self):
        self.popularity = self.puzzle['Popularity']

    def get_NbPlays(self):
        self.nb_plays = self.puzzle['NbPlays']

    def get_Themes(self):
        self.themes = self.puzzle['Themes']

    def Attributs(self):
        self.get_Fen()
        self.get_Id()
        self.get_Moves()
        self.get_RatingDeviation()
        self.get_Popularity()
        self.get_NbPlays()
        self.get_Themes()

