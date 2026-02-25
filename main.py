import sys
from PySide6.QtWidgets import QApplication

from model.file_loader import FileLoader
from model.Puzzle import Puzzle
from model.fen import FEN
from view.view import ChessBoard

def main():
    loader = FileLoader("lichess.csv")
    all_puzzles = loader.readCSV()
    
    if all_puzzles:
        my_puzzle = Puzzle(all_puzzles[0])
        my_puzzle.puzzle = all_puzzles[0] 
        my_puzzle.Attributs()

        fen_logic = FEN(my_puzzle.Fen)
        new_grid = fen_logic.to_grid()

        app = QApplication(sys.argv)
        window = ChessBoard()

        window.board_model = new_grid
        window.update_view()
        
        window.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    main()