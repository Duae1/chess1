import sys 
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.file_loader import FileLoader

def test_file_loader():
  data = FileLoader("Lichess.csv").read_csv()

  assert data is not None, "Pas de retour None"
  assert isinstance(data, list), "Il faut un retour liste"
  assert len(data)>0:
    print("Fichier chargé ")

  nodata = FileLoader("").read_csv()

  assert nodata == []
  print("Test fichier manquant OK")

if __name__ == "__main__":
    test_file_loader()
