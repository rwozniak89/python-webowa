def witacz():
    print('witaj')

class Autor:
    imie = None
    nazwisko = None
    opis = None

    def __init__(self, i, n, o):
        self.imie = i
        self.nazwisko = n
        self.opis = o