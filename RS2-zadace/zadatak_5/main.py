from shop.proizvodi import dodaj_proizvod, proizvodi
from shop.narudzbe import napravi_narudzbu

novi_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for p in novi_proizvodi:
    dodaj_proizvod(p["naziv"], p["cijena"], p["kolicina"])

for proizvod in proizvodi:
    proizvod.ispis()

narudzba = napravi_narudzbu(novi_proizvodi)
if narudzba:
    narudzba.ispis_narudzbe()