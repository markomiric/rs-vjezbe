nizovi = ["jabuka", "kruška", "banana", "naranča"]
kvadrirane_duljine = list(map(lambda x: len(x) ** 2, nizovi))
print(kvadrirane_duljine)  # [36, 36, 36, 49]

brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
veci_od_5 = list(filter(lambda x: x > 5, brojevi))
print(veci_od_5)  # [21, 33, 45, 9, 10]

brojevi = [10, 5, 12, 15, 20]
transform = dict(map(lambda x: (x, x**2), brojevi))
print(transform)  # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]
svi_punoljetni = all(map(lambda x: x["godine"] >= 18, studenti))
print(svi_punoljetni)  # False

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
          "pjesma", "otorinolaringolog"]
min_duljina = int(input("Unesite minimalnu duljinu riječi: "))
duge_rijeci = list(filter(lambda x: len(x) > min_duljina, rijeci))
print(duge_rijeci)  # ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']