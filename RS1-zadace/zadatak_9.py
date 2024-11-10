def ukloni_duplikate(lista):
    return list(set(lista))

def test_ukloni_duplikate():
    # Test 1: Lista s duplikatima brojeva
    lista1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    print(f"Test 1 - Lista s duplikatima: {lista1}")
    print(f"Lista bez duplikata: {ukloni_duplikate(lista1)}\n")
    
    # Test 2: Prazna lista
    lista2 = []
    print(f"Test 2 - Prazna lista: {lista2}")
    print(f"Lista bez duplikata: {ukloni_duplikate(lista2)}\n")
    
    # Test 3: Lista sa stringovima
    lista3 = ["a", "b", "a", "c", "b", "d"]
    print(f"Test 3 - Lista stringova: {lista3}")
    print(f"Lista bez duplikata: {ukloni_duplikate(lista3)}\n")
    
    # Test 4: Lista bez duplikata
    lista4 = [1, 2, 3, 4, 5]
    print(f"Test 4 - Lista bez duplikata: {lista4}")
    print(f"Lista bez duplikata: {ukloni_duplikate(lista4)}")

if __name__ == "__main__":
    test_ukloni_duplikate()