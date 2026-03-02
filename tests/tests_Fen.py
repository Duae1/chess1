import sys 
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.fen import Fen 

def test_fen(): 
    
    fen_valide = Fen("5rk1/1p3ppp/pq3b2/8/8/1P1Q1N2/P4PPP/3R2K1 w - - 2 27").to_grid()
    
    assert fen_valide is not None
    assert len(fen_valide) == 8 and len(fen_valide[0]) == 8
    print("Test FEN classique : OK")

    fen_invalide = Fen("test/5rk1/1p3ppp 7 w -- 4").to_grid()
    
    assert fen_invalide is None
    print("Test FEN incorrect : OK")

    # On teste avec deux cavaliers
    fen_vide = Fen("8/8/8/4N3/3n4/8/8/8 w - - 0 1").to_grid()

    assert fen_vide is not None, "La grille doit être générée même avec peu de pièces"
    assert len(fen_vide) == 8 and len(fen_vide[0]) == 8, "La taille reste 8x8"
    assert fen_vide[0] == [None, None, None, None, None, None, None, None]
    print("Test FEN avec 2 pièces (petits exos) : OK")

if __name__ == "__main__":
    test_fen()
