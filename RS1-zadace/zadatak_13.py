def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])

def maks_i_min(lista):
    maks = lista[0]
    mini = lista[0]
    
    for broj in lista:
        if broj > maks:
            maks = broj
        if broj < mini:
            mini = broj
    return (maks, mini)

def presjek(skup1, skup2):
    return skup1 & skup2

def test_funkcije():
    # Test prvi_i_zadnji
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Test prvi_i_zadnji:")
    print(f"Ulaz: {lista1}")
    print(f"Rezultat: {prvi_i_zadnji(lista1)}\n")

    # Test maks_i_min
    lista2 = [5, 10, 20, 50, 100, 11, 250, 50, 80]
    print("Test maks_i_min:")
    print(f"Ulaz: {lista2}")
    print(f"Rezultat: {maks_i_min(lista2)}\n")

    # Test presjek
    skup1 = {1, 2, 3, 4, 5}
    skup2 = {4, 5, 6, 7, 8}
    print("Test presjek:")
    print(f"Skup 1: {skup1}")
    print(f"Skup 2: {skup2}")
    print(f"Rezultat: {presjek(skup1, skup2)}")

if __name__ == "__main__":
    test_funkcije()