# w konsoli komenda pytest albo pytest nazwa_pliku, pytest szuka plikow o nazwie test_... i robi testy z tego pliku

#pytest
#pytest nazwa pliku # tylko testy z tego pliku
#pytest -v #wiecej szczegółów
#pytest -v -m sekcja # odpalenie okreslonych sekcji

import biblioteka
import pytest


#@pytest.mark.sekcja1
def test_dodawanie():
    assert biblioteka.dodawanie(10, 10) == 20


#@pytest.mark.sekcja1
def test_odejmowanie():
    assert biblioteka.odejmowanie(10, 10) == 0


#@pytest.mark.sekcja2
def test_mnozenie():
    assert biblioteka.mnozenie(2, 2) == 4


#@pytest.mark.sekcja2
def test_dzielenie():
    assert biblioteka.dzielenie(10, 5) == 2

def test_lista():
    assert len(biblioteka.lista())>0

#Napisz testy jednostkowe do naszego DAO dotyczącego pracowników.
#Testom ma podlegać funkcja pobierz_pracownikow() - sprawdź czy długość zwracanej listy jest większa od 0
#oraz funkcja pobierz_pracownika(id) - sprawdź czy zwracany obiekt ma wszystkie pola uzupełnione (oczywiście
#testując do metody pobierz_pracownika przekaz id jakiegoś istniejącego pracownika mającego wszystkie pola
#uzupełnione.

import modulPracownicy

def test_dao_pobierz_pracownikow():
    wynik = modulPracownicy.pobierz_pracownikow()
    print(wynik)
    assert len(wynik)>0

def test_dao_pobierz_pracownika():
    p = modulPracownicy.pobierz_pracownika(5)
    ok = True
    if p.id_pracownika is None:
        ok=False
    if p.imie is None or len(p.imie)== 0:
        ok=False
    if p.nazwisko is None or len(p.nazwisko)== 0:
        ok=False
    if p.email is None or len(p.email)== 0:
        ok=False

    assert ok
