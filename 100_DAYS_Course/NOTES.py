import numpy as np

class Klasa:
    def __init__(self, var1=0, var2=0, name='None'):
        self.var1 = var1
        self.var2 = var2
        self.name = name
    def show(self):
        print("Calość zmiennych : var1 {} var2 {} name {} \n".format(self.var1, self.var2, self.name))


class Pochodna(Klasa):
    def show(self):
        print("Calość zmiennych w pochodnej : var1 {} var2 {} name {} \n".format(self.var1, self.var2, self.name))


k = Klasa()
k.show()
k1 = Klasa(2, 3, 'nazwa')
p1 = Pochodna(2, 3, 'pochodna')

k1.show()
p1.show()

# dictionaries
cubes = {x: x*x*x for x in range(5)}  # dictionary comprehension
print(cubes[2])
print(cubes)
# mozna przez update zmieniac lub dodawac lub zmieniac elementy ale jak zmieniac to tylko wartosci dla danego klucza
cubes.update({2: 9})
print(cubes)


# set
# dane nie sa uporzadkowane ( printuje sie w losowej kolejnosci)  i sie nie powtarzaja , jedna zmienna pojawia sie w secie tylko raz
sett = {"name", "surname"}
sett.add("name")
print(sett)


# list comprehension and generators i tuple
lista = [x for x in range(10)]
gen = (x for x in range(10))   # tworzy i zwraca obiekt generatora który bedzie dawać wartości wtedy kiedy bedie to konieczne
                               # ale działa to jak tupla wiec nie mozna zmieniac konkretynych wartocji bo tu ich jeszcze wgl nie ma
tupla = (1, 2, 3, 5)     # typla jest immutable wiec juz nie mozna tutaj zmeiniac wartosci

# Generator generuje jeden przedmiot na raz i generuje przedmiot tylko wtedy, gdy jest na to popyt.
# Podczas gdy w rozumieniu listy Python rezerwuje pamięć dla całej listy.
# Możemy więc powiedzieć, że wyrażenia generatora są bardziej wydajne pod względem pamięci niż listy.
for i in gen:
    print(i, end=' ')

# is vs ==
str1 = [1, 2, 3]
str2 = str1[:]
print("\n", str1 == str2)
print(str1 is str2)


#  #   jakis przykładowy fixture czyli specjalnie oznaczona funkcja która zostanie wywołana przed wykonaniem testu
#         np. moze byc tak ze ta funkcja musi sie wykonać przed przbiegiem testu aby były dane do testów
# @pytest.fixture()
# def csv_data():
#     with open('book.csv') as f:
#         data = f.read().split('\n')
#     return data


### wątki w pythonie
def count(name):
    for i in range(1000):
        print(str(i) + name + "\n")

import threading
##  multiple threads in a loop
names = ["thread_1", "thread_2", "thread_3"]

for name in names:
    thread = threading.Thread(target=count, args=(name, ))
    thread.start()
    # thread.join()

