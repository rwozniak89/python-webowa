
class Pracownik:
    id_pracownika = None
    imie = None
    nazwisko = None
    email = None

    def __init__(self, id, im, na, em):
        self.id_pracownika = id
        self.imie = im
        self.nazwisko = na
        self.email = em

    def __str__(self):
        return f'id_pracownika={self.id_pracownika}, imie={self.imie}, nazwisko={self.nazwisko}, email={self.email}'

import psycopg2

def pobierz_pracownikow():
    polaczenie = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="1qazXSW@",
                                  port=5432)
    kursor = polaczenie.cursor()
    wynik = list()
    try:
        sql = 'select * from pracownicy order by id_pracownika'
        kursor.execute(sql)
        for w in kursor:
            wynik.append(Pracownik(w[0], w[1], w[2], w[3]))
    except Exception as e:
        print(e)
        polaczenie.rollback()
    kursor.close()
    polaczenie.close()
    return wynik

def test_pobierania():
    lista = pobierz_pracownikow()
    for e in lista:
        print(e)

##test_pobierania()


def pobierz_pracownika(id):
    polaczenie = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="1qazXSW@",
                                  port=5432)
    kursor = polaczenie.cursor()
    sql = f'select * from pracownicy where id_pracownika={id}'
    kursor.execute(sql)
    w = kursor.fetchone()
    p=Pracownik(w[0], w[1], w[2], w[3])
    # print(f'pobrano pracownika {p}')
    kursor.close()
    polaczenie.close()
    return p

def nowy_pracownik(p):
    polaczenie = psycopg2.connect(host='localhost', database='postgres', user="postgres", password="1qazXSW@", port=5432)
    kursor = polaczenie.cursor()
    sql=f"insert into pracownicy(imie,nazwisko,email) values ('{p.imie}','{p.nazwisko}','{p.email}')"
    kursor.execute(sql)
    polaczenie.commit()
    kursor.close()
    polaczenie.close()

def aktualizuj_pracownika(p):
    polaczenie = psycopg2.connect(host='localhost', database='postgres', user="postgres", password="1qazXSW@", port=5432)
    kursor = polaczenie.cursor()
    sql=f"update pracownicy set imie='{p.imie}', nazwisko='{p.nazwisko}', email='{p.email}' where id_pracownika={p.id_pracownika}"
    kursor.execute(sql)
    polaczenie.commit()
    kursor.close()
    polaczenie.close()

def usun_pracownika(id):
    polaczenie = psycopg2.connect(host='localhost', database='postgres', user="postgres", password="1qazXSW@",
                                  port=5432)
    kursor = polaczenie.cursor()
    sql = f"delete from pracownicy where id_pracownika={id}"
    kursor.execute(sql)
    polaczenie.commit()
    kursor.close()
    polaczenie.close()
#