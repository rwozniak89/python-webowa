import sqlalchemy
from flask import Flask

#from modul import witacz

app = Flask(__name__)

#witacz()

# @app.route('/')
# def hello_world():
#     return '<h1>Hej Hejka  Siemanko!!!</h1>'
#
#
# if __name__ == '__main__':
#     app.run(debug=True, port=80) ##uruchamiać z poziomu terminala python app.py

#1. Dodaj obsługę adresów /zawodnicy i /pracownicy. Obsługa każdego z adresów ma się
#   sprowadzać do wyświetlenia szablonowego pliku html - powinny to być osobne pliki html

# from flask import Flask,render_template
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     #return '<h1>hello!</h1>'
#     return render_template("index.html")
#
# @app.route('/zawodnicy')
# def zawodnicy():
#     return render_template('zawodnicy.html')
#
# @app.route('/pracownicy')
# def pracownicy():
#     return render_template('pracownicy.html')
#
# if __name__ == '__main__':
#     app.run(debug=True,port=80)

##################################################3

from flask import Flask, render_template,request,redirect,session
from modul import Autor
from modulPracownicy import *
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY']='ciąg tekstowy'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1qazXSW@@localhost/postgres'

db=SQLAlchemy(app)


lista = ['test1', 'element2', 'cos tam ma nr 3']
@app.route('/')
def index():
    return render_template("index.html",imie='Rad',nazwisko='Woz', lista=lista)

@app.route('/wyszukiwarka')
def wyszukiwarka():
    return render_template('wyszukiwarka.html')

@app.route('/wyszukiwarka',methods=['POST'])
def wyszukiwarka_post():
    import os
    fraza = request.form['fraza']
    print(fraza)
    wynik = []
    for p in os.walk('d:\\'):
        for e in p[1]:
            if fraza in e:
                print(f'{p[0]}\{e}')
                wynik.append(f'{p[0]}\{e}')
        for f in p[2]:
            if fraza in f:
                print(f'{p[0]}\{f}')
                wynik.append(f'{p[0]}\{f}')
    return render_template('wyszukiwarka.html', wynik=wynik, fraza=fraza)


@app.route('/wynik')
def wynik():
    return render_template('wynik.html')

@app.route('/usluga_sieciowa') #jak api
def usluga_sieciowa():
    data=dict()
    data['klucz']='wartość'
    return data

@app.route('/wykres')
def wykres():
    lista1 = [pow(2, e) for e in range(10)]
    plt.plot(lista1)
    plt.savefig('static/wykres.png')
    # plt.show()
    return "<img src='static/wykres.png'/>"

@app.route('/get_random')
def get_random():
    import random
    x=random.randint(1, 100)
    print(x)
    return str(x)

@app.route('/refresher')
def refresher():
    return render_template("refresher.html")


@app.errorhandler(404)
def error404(e):
    return "Brak"


class Zawodnik(db.Model):
    __tablename__="zawodnicy"
    id_zawodnika=db.Column(db.Integer, name="id_zawodnika",primary_key=True)
    imie=db.Column(db.String,name='imie', nullable=True)#unique=True)
    nazwisko=db.Column(db.String,name='nazwisko')
    wzrost=db.Column(db.Numeric, name="wzrost")
    masa=db.Column(db.Numeric,name='masa')

    def __str__(self):
        return f'id_zawodnika={self.id_zawodnika}, imie={self.imie}, nazwisko={self.nazwisko}, wzrost={self.wzrost}, masa={self.masa}'

def zapisz_zawodnika(zawodnik):
    db.session.add(zawodnik)
    db.session.commit()

def daj_zawodnika(id):
    return Zawodnik.query.filter(Zawodnik.id_zawodnika==id).first()

def daj_zawodnikow():
    return Zawodnik.query.all()

def daj_zawodnikow_sort_po_id():
    q=Zawodnik.query.order_by(Zawodnik.id_zawodnika.desc())
    print(f'Zapytanie: {q}')
    return q.all()

def daj_grubszych():
    return Zawodnik.query.filter(Zawodnik.masa>70).all()

def zapisz_zawodnika(zawodnik):
    db.session.add(zawodnik)
    db.session.commit()

def kasuj_zawodnika(zawodnik):
    db.session.delete(zawodnik)
    db.session.commit()

# class Przykladowa(db.Model):
#     pole1=db.Column(db.Integer, primary_key=True)
#     pole2=db.Column(db.String)
#
# @app.route('/tworz_tabele')
# def tworz_tabele():
#     db.create_all()
#     return "<h1>Tabele stworzone</h1>"


@app.route('/zawodnicy')
def zawodnicy():
    lista = daj_zawodnikow_sort_po_id()
    for z in lista:
        print(z)
    return render_template('zawodnicy.html')


@app.route('/pracownicy')
def pracownicy():
    try:
        zalogowany=session['logged']
    except:
        return redirect('/logowanie')

    print(f"########## {session['logged']}")
    return render_template('pracownicy.html', lista = pobierz_pracownikow())

@app.route('/pracownik')
def pracownik():
    id= request.args.get('id')
    print(f'odebrane id={id}')
    p = pobierz_pracownika(id)
    print(p)
    return render_template('pracownik.html', pracownik = p)

@app.route('/dodaj_pracownika')
def dodaj_pracownika():
    return render_template('dodaj_pracownika.html')

@app.route('/dodaj_pracownika',methods=['POST'])
def dodaj_pracownika_post():
    imie=request.form['imie']
    nazwisko=request.form['nazwisko']
    email=request.form['email']
    #print(f'imie={imie}, nazwisko={nazwisko}, email={email}')
    p=Pracownik(None,imie,nazwisko,email)
    nowy_pracownik(p)
    return redirect('/pracownicy')

@app.route('/edytuj_pracownika')
def edytuj_pracownika():
    id=request.args.get('id')
    p=pobierz_pracownika(id)
    print(p)
    return render_template("edytuj_pracownika.html", pracownik = p)

@app.route('/edytuj_pracownika',methods=['POST'])
def edytuj_pracownika_post():
    id=request.form['id_pracownika']
    imie = request.form['imie']
    nazwisko = request.form['nazwisko']
    email = request.form['email']
    p = Pracownik(id, imie, nazwisko, email)
    print(p)
    aktualizuj_pracownika(p)
    return redirect('/pracownicy')

# kasuj_pracownika
@app.route('/kasuj_pracownika')
def kasuj_pracownika():
    id = request.args.get('id')
    p = pobierz_pracownika(id)
    return render_template('/kasuj_pracownika.html', pracownik=p)

@app.route('/kasuj_pracownika',methods=['POST'])
def kasuj_pracownika_post():
    id = request.form['id_pracownika']
    print(f'kasowanie pracownika o id {id}')
    usun_pracownika(id)
    return redirect('/pracownicy')

@app.route('/logowanie')
def logowanie():
    return render_template('/logowanie.html')

@app.route('/logowanie',methods=['POST'])
def logowanie_post():
    login = request.form['login']
    password = request.form['password']
    print(login, password)
    session['logged']=login
    return redirect('/pracownicy')

@app.route('/autor')
def akcjaautor():
    return render_template('autor.html', autor=Autor('Radek', 'Woz', 'super opis ma'))


@app.route('/watkuj')
def watkuj():
    import time
    import threading

    def osobny_watek(nazwa_watku):
        i = 0;
        while True:
            time.sleep(0.01)
            i += 1
            print(f'siema tu osobny wątek {i} o nazwie {nazwa_watku}')
            if i == 25:
                break

    t = threading.Thread(target=osobny_watek, args=('nazwa_watku',))
    print('tu główny wątek Start')
    t.start()
    for x in range(2):
        print(f'tu główny wątek {x}')
        time.sleep(0.5)

    return "OK - wątek uruchmiony"


if __name__ == '__main__':
    app.run(debug=True,port=80)

#2. Do projektu dodaj klasę Autor która będzie posiadała imię , nazwisko i opis jako pola. Klasa ta
#   powinna zawierać konstruktor sparametryzowany. Do projektu dodaj podstronę "O autorze"
#   do której przekażemy obiekt klasy Autor i wyświetlimy zawarte w nim dane.

#3 pracownicy wyswietlic nowy widok

#4 wyswietlicz szczegoly pracownika
