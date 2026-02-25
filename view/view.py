import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QGridLayout
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QPainter, QColor


# Dictionnaire des pièces en Unicode
PIECES = {
    "r": "\u265C",  # tour noire
    "n": "\u265E",  # cavalier noir
    "b": "\u265D",  # fou noir
    "q": "\u265B",  # dame noire
    "k": "\u265A",  # roi noir
    "p": "\u265F",  # pion noir

    "R": "\u2656",  # tour blanche
    "N": "\u2658",  # cavalier blanc
    "B": "\u2657",  # fou blanc
    "Q": "\u2655",  # dame blanche
    "K": "\u2654",  # roi blanc
    "P": "\u2659",  # pion blanc
}


class Square(QLabel):
    """Une case du plateau"""
    
    clicked = Signal(int, int)
    
    def __init__(self, row, col, color):
        super().__init__()
        self.row = row
        self.col = col
        self.base_color = color

        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(80, 80)
        self.setStyleSheet(f"background-color: {color};")
        self.setFont(QFont("DejaVu Sans", 36))
        
    def mousePressEvent(self, event):
        self.clicked.emit(self.row, self.col)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QColor(100, 100, 100)) 
        painter.setFont(QFont("Arial", 10, QFont.Bold))
        if self.col == 0:
            painter.drawText(3, 12, str(8 - self.row))
        if self.row == 7:
            painter.drawText(68, 77, "abcdefgh"[self.col])
        painter.end()


class ChessBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Échecs – GridLayout (minimal)")

        self.selected_square = None

        self.board_model = self.init_board()
        self.grid = QGridLayout(self)
        self.grid.setSpacing(0)

        self.squares = [["" for _ in range(8)] for _ in range(8)]
        self.create_board()
        self.update_view()

    def init_board(self):
        return [
            ["r","n","b","q","k","b","n","r"],
            ["p"] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            ["P"] * 8,
            ["R","N","B","Q","K","B","N","R"],
        ]

    def create_board(self):
        for row in range(8):
            for col in range(8):
                color = "#EEEED2" if (row + col) % 2 == 0 else "#769656"
                square = Square(row, col, color)
                square.clicked.connect(self.on_square_clicked)
                self.grid.addWidget(square, row, col)
                self.squares[row][col] = square

    def on_square_clicked(self, row, col):
        piece = self.board_model[row][col]

        # Sélection
        if self.selected_square is None:
            if piece is not None:
                self.selected_square = (row, col)
        else:
            src_row, src_col = self.selected_square

            # Déplacement simple (sans règles)
            self.board_model[row][col] = self.board_model[src_row][src_col]
            self.board_model[src_row][src_col] = None

            self.selected_square = None
            self.update_view()

    def update_view(self):
        for row in range(len(self.squares)):
            for col in range(len(self.squares[0])):
                piece = self.board_model[row][col]
                self.squares[row][col].setText(PIECES.get(piece, ""))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChessBoard()
    window.show()
    sys.exit(app.exec())
