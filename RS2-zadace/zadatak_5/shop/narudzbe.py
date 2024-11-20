class Narudzba:
    def __init__(self, proizvodi, ukupna_cijena):
        self.proizvodi = proizvodi
        self.ukupna_cijena = ukupna_cijena
    
    def ispis_narudzbe(self):
        proizvodi_str = ", ".join([f"{p['naziv']} x {p['kolicina']}" for p in self.proizvodi])
        print(f"Naručeni proizvodi: {proizvodi_str}, Ukupna cijena: {self.ukupna_cijena} eur")

narudzbe = []

def napravi_narudzbu(proizvodi):
    if not isinstance(proizvodi, list):
        raise ValueError("Argument proizvodi mora biti lista")
    if not proizvodi:
        raise ValueError("Lista ne smije biti prazna")
    if not all(isinstance(p, dict) for p in proizvodi):
        raise ValueError("Svaki element mora biti rječnik")
    if not all(all(k in p for k in ['naziv', 'cijena', 'kolicina']) for p in proizvodi):
        raise ValueError("Svaki rječnik mora sadržavati naziv, cijena i kolicina")
    
    # Provjera dostupnosti
    for proizvod in proizvodi:
        if proizvod['kolicina'] <= 0:
            print(f"Proizvod {proizvod['naziv']} nije dostupan!")
            return None
    
    # Kreiranje narudžbe
    ukupna_cijena = sum(p['cijena'] * p['kolicina'] for p in proizvodi)
    narudzba = Narudzba(proizvodi, ukupna_cijena)
    narudzbe.append(narudzba)
    return narudzba