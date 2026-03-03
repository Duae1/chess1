class Fen:
    def __init__(self, fen_string : str) -> None:
        self.fen_string = fen_string

    def is_valid(self) -> bool:
        parts = self.fen_string.split(' ')
        if not parts or parts[0] == "": # si la chaîne est vide false
            return False
        board_layout = parts[0]
        
        rows = board_layout.split('/')
        if len(rows) != 8:
            return False
            
        for row in rows:
            count = 0
            for char in row:
                if char.isdigit():
                    count += int(char)
                elif char.isalpha(): #  Vérifie que c'est bien une LETTRE
                    count += 1    
                else:
                    return False 
            
            if count != 8:
                return False
        
        return True

    def to_grid(self):
        """Converts the FEN string into an 8x8 list for the board"""
        if not self.is_valid(): #  Empêche de créer une grille si le FEN est faux
            return None
        board_part = self.fen_string.split(' ')[0]
        grid = []
        
        for row in board_part.split('/'):
            grid_row = []
            for char in row:
                if char.isdigit():
                    # If it's '8', add 8 empty squares
                    grid_row.extend([None] * int(char))
                else:
                    grid_row.append(char)
            grid.append(grid_row)

        return grid
