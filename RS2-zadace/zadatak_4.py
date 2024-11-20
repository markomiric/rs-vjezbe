from datetime import datetime
from math import sqrt, pi

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza
    
    def ispis(self):
        print(f"Marka: {self.marka}\nModel: {self.model}\n"
              f"Godina proizvodnje: {self.godina_proizvodnje}\n"
              f"Kilometraža: {self.kilometraza}")
    
    def starost(self):
        return datetime.now().year - self.godina_proizvodnje

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self): return self.a + self.b
    def oduzimanje(self): return self.a - self.b
    def mnozenje(self): return self.a * self.b
    def dijeljenje(self): return self.a / self.b
    def potenciranje(self): return self.a ** self.b
    def korijen(self): return sqrt(self.a), sqrt(self.b)

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
    
    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = [Student(**student) for student in studenti]
najbolji_student = max(studenti_objekti, key=lambda x: x.prosjek())

class Krug:
    def __init__(self, r):
        self.r = r
    
    def opseg(self):
        return 2 * self.r * pi
    
    def povrsina(self):
        return self.r ** 2 * pi

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    
    def work(self):
        print(f"Radim na poziciji {self.pozicija}")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
    
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
    
    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje


auto = Automobil("Toyota", "Corolla", 2018, 50000)
auto.ispis()
print(f"Starost automobila: {auto.starost()} godina")

kalkulator = Kalkulator(10, 5)
print(f"Zbroj: {kalkulator.zbroj()}")

krug = Krug(5)
print(f"Opseg: {krug.opseg():.2f}")
print(f"Površina: {krug.povrsina():.2f}")

radnik = Radnik("Ivan", "Programer", 10000)
manager = Manager("Ana", "Voditelj", 15000, "IT")
radnik.work()
manager.work()
manager.give_raise(radnik, 1000)
print(f"Nova plaća: {radnik.placa}")