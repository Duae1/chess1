class FEN:
    def __init__(self, fen):
        self.fen = fen

    def is_valid(self):
        parts = self.fen.split(' ')
        board_layout = parts[0]
        
        rows = board_layout.split('/')
        if len(rows) != 8:
            return False
            
        for row in rows:
            count = 0
            for char in row:
                if char.isdigit():
                    count += int(char)
                else:
                    count += 1
            
            if count != 8:
                return False
        
        return True

    def to_grid(self):
        """Converts the FEN string into an 8x8 list for the board"""
        board_part = self.fen.split(' ')[0]
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