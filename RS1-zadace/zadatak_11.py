def grupiraj_po_paritetu(lista):
    rezultat = {
        'parni': [],
        'neparni': []
    }
    
    for broj in lista:
        if broj % 2 == 0:
            rezultat['parni'].append(broj)
        else:
            rezultat['neparni'].append(broj)
            
    return rezultat

def test_grupiraj_po_paritetu():
    # Test 1: Standard list 1-10
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Test 1 - Standardna lista:")
    print(f"Ulaz: {lista1}")
    print(f"Rezultat: {grupiraj_po_paritetu(lista1)}\n")
    
    # Test 2: Empty list
    lista2 = []
    print("Test 2 - Prazna lista:")
    print(f"Ulaz: {lista2}")
    print(f"Rezultat: {grupiraj_po_paritetu(lista2)}\n")
    
    # Test 3: Only even numbers
    lista3 = [2, 4, 6, 8, 10]
    print("Test 3 - Samo parni brojevi:")
    print(f"Ulaz: {lista3}")
    print(f"Rezultat: {grupiraj_po_paritetu(lista3)}\n")
    
    # Test 4: Only odd numbers
    lista4 = [1, 3, 5, 7, 9]
    print("Test 4 - Samo neparni brojevi:")
    print(f"Ulaz: {lista4}")
    print(f"Rezultat: {grupiraj_po_paritetu(lista4)}")

if __name__ == "__main__":
    test_grupiraj_po_paritetu()