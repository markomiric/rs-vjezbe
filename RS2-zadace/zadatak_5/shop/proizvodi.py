class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina
    
    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena}, Količina: {self.kolicina}")

proizvodi = [
    Proizvod("Računalo", 3000, 5),
    Proizvod("Printer", 800, 10)
]

def dodaj_proizvod(naziv, cijena, kolicina):
    novi_proizvod = Proizvod(naziv, cijena, kolicina)
    proizvodi.append(novi_proizvod)
    return novi_proizvod