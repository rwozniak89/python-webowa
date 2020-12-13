import time
import threading

# def osobny_watek(nazwa_watku):
#     i =0;
#     while True:
#         time.sleep(1)
#         i+= 1
#         print(f'siema tu osobny wątek {i} o nazwie {nazwa_watku}')
#
# t=threading.Thread(target=osobny_watek, args=('nazwa_watku',))
# print('tu główny wątek1')
# t.start()
# for x in range(10):
#     print('tu główny wątek2')
#     time.sleep(1)


#stworzyc funckje i wywolac ją w roznych wątkach

# import time
# import threading
#
# def funkcja_wyswietl(nazwa):
#     print(f'początek wątku {nazwa}')
#     time.sleep(1)
#     print(f'koniec wątku {nazwa}')
#
#
# watki = []
# for x in range(10):
#     t = threading.Thread(target=funkcja_wyswietl, args=(f'fun numer{x}',))
#     watki.append(t)
#
# for i in watki:
#     i.start()

# pip install numpy==1.19.3
# import matplotlib.pyplot as plt
#
# lista1 = [pow(2, e) for e in range(5)]
# lista2 = [pow(3, e) for e in range(5)]
# plt.plot(lista1)
# plt.plot(lista2)
# plt.savefig('static/wykres.png')
# plt.show()
#
# import matplotlib.pyplot as plt
# import numpy as np
# lista1=[pow(2,e) for e in range(3)]
# lista2=np.sin(lista1)
# plt.plot(lista1)
# plt.plot(lista2)
# plt.savefig('static/wykres.png')
# plt.show()
#
#
# import matplotlib.pyplot as plt
# import numpy as np
# lista1=[pow(2,e) for e in range(5)]
# lista2=[pow(3,e) for e in range(5)]
# plt.plot(lista1,label="LISTA 1")
# plt.plot(lista2,label="LISTA 2")
# plt.legend()
# plt.xlabel('oś X')
# plt.ylabel('oś Y')
# plt.savefig('static/wykres.png')
# plt.show()
#
# import matplotlib.pyplot as plt
# import numpy as np
# lista1=[pow(2,e) for e in range(5)]
# lista2=[pow(3,e) for e in range(5)]
# plt.plot(lista1,'g--',  label="LISTA 1")
# plt.plot(lista2,'r:',label="LISTA 2")
# plt.legend()
# plt.xlabel('oś X')
# plt.ylabel('oś Y')
# #plt.savefig('static/wykres.png')
# plt.grid()
# plt.show()

# import matplotlib.pyplot as plt
# from random import random
# x=[e for e in range(10)]
# y=[random()*10000 for e in range(10)]
# plt.bar(x,y)
# plt.show()


# import os
# for p in os.walk('C:\\'):
#     print(f'#########   KATALOG: {p[0]}')
#     print('PODKATALOGI:')
#     for k in p[1]:
#         print(k)
#     print('PLIKI:')
#     for pp in p[2]:
#         print(pp)
# #import os
# #help(os.walk)

import os
# if os.path.exists('d:\\hello.txt'):
#     print('plik istnieje')
# else:
#     print('plik nie istnieje')
#
# if os.path.isdir('d:\\hello.txt'):
#     print('to jest katalog')
# else:
#     print('to jest plik')
#
# if os.path.isfile('d:\\hello.txt'):
#     print('to jest plik')
# else:
#     print('to jest katalog')

# os.chdir('d:\\')
# print(os.getcwd())
# print(os.listdir())

# print(os.path.getsize('d:\\hello.txt'))

#os.mkdir('d:\\nowy')
#os.rmdir('d:\\nowy')
#os.remove('d:\\pliczek.txt')


#Robimy wyszukiwarkę plików
#Do naszej aplikacji dodaj formularz z jednym polem tekstowym i guzikiem szukaj.
#Po zatwierdzeniu formularza przez uzytkownika powinnismy zostac przekierowani
#do strony na której będą wyświetlone wszystkie pliki wraz ze ścieżkami które
#będą miały w nazwie frazę wpisaną w pole tekstowe formularza.

# zrobione w app.py jako wyszukiwarka

# class MyDictionary:
#     dict = dict()
#
#     def dodaj_element(self, klucz, wartosc):
#         self.dict[klucz] = wartosc
#     def daj_element(self, klucz):
#         return  self.dict[klucz]
#
# ms = MyDictionary()
# ms.dodaj_element('przyklad', 'wartosc')
# print( ms.daj_element('przyklad') )

# class MyDictionary:
#     dict = dict()
#
#     def __setitem__(self, key, value):
#         self.dict[key] = value
#     def __getitem__(self, key):
#         return  self.dict[key]
#
# ms= MyDictionary()
# ms['klucz'] = 'wartosc'
# print(ms['klucz'])

# zmienna='COŚ'
# def funkcja():
#     global zmienna
#     print(f'zmienna={zmienna}')
#
# funkcja()

tekst ='asdasdsafa asdas dsaADSasda - ; saassa 1  22121 1212 1122 22  11 dsadsdadsa'
import re

# print(re.findall('.',tekst))
# print(re.findall('\d',tekst))
# print(re.findall('\D',tekst))
# print(re.findall('\w',tekst))
# print(re.findall('\W',tekst))
# print(re.findall('\-|;',tekst))
# print(re.findall('[1-2]',tekst))
# print(re.findall('[a-g]',tekst))
# print(re.findall('[A-G]',tekst))
# print(re.findall('[a-gA-G]',tekst))
# print(re.findall('[^a-g]',tekst))
# print(re.findall('\d*',tekst))
# print(re.findall('\d{3}',tekst))
# # print(re.findall('\d*',tekst))
# print(re.findall('\d{2,}',tekst))
# print(re.findall('\d{1,5}',tekst))
# print(re.findall('\d{,2}
# print(re.findall('[\d| ]{5,}',tekst))

# import requests
# from bs4 import BeautifulSoup
# strona = requests.get('http://jsystems.pl')
