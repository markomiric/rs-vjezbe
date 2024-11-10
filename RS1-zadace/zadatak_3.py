import random

trazeni_broj = random.randint(1, 100)
broj_je_pogoden = False
broj_pokusaja = 0

while not broj_je_pogoden:
    pokusaj = int(input("Pogodi broj (1-100): "))
    broj_pokusaja += 1
    
    if pokusaj < trazeni_broj:
        print("Broj je veći!")
    elif pokusaj > trazeni_broj:
        print("Broj je manji!")
    else:
        broj_je_pogoden = True
        print(f"Bravo, pogodio si u {broj_pokusaja} pokušaja!")