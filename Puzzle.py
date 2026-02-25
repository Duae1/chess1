class Puzzle:
    def __init__(self, dict_data):
        self.puzzle = dict_data
        self.Fen = None
        self.Id = None
        self.Moves = None
        self.RatingDeviation = None
        self.Popularity = None
        self.nbPlays = None
        self.Themes = None

    def get_FEN(self):
        self.Fen = self.puzzle['FEN']

    def get_Id(self):
        self.Id = self.puzzle['PuzzleId']

    def get_Moves(self):
        self.Moves = self.puzzle['Moves']

    def get_RatingDeviation(self):
        self.RatingDeviation = self.puzzle['RatingDeviation']

    def get_Popularity(self):
        self.Popularity = self.puzzle['Popularity']

    def get_nbPlays(self):
        self.nbPlays = self.puzzle['NbPlays']

    def get_Themes(self):
        self.Themes = self.puzzle['Themes']

    def Attributs(self):
        self.get_FEN()
        self.get_Id()
        self.get_Moves()
        self.get_RatingDeviation()
        self.get_Popularity()
        self.get_nbPlays()
        self.get_Themes()