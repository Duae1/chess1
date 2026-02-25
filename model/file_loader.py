import csv

class FileLoader:
    def __init__(self, file_path):
        self.file_path=file_path
        self.dico=[]

    def readCSV(self):
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                csv_reader=csv.DictReader(file)
                self.dico=[row for row in csv_reader]
            print("Dico is created")
            return self.dico
        except FileNotFoundError:
            print(f"Error: Could not find the file at {self.file_path}")
            return None

