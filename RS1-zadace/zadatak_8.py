def filtriraj_parne(lista):
    return [broj for broj in lista if broj % 2 == 0]

def main():
    # Test case 1: Basic list 1-10
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original lista: {lista1}")
    print(f"Parni brojevi: {filtriraj_parne(lista1)}")
    
    # Test case 2: Empty list
    lista2 = []
    print(f"\nPrazna lista: {lista2}")
    print(f"Parni brojevi: {filtriraj_parne(lista2)}")
    
    # Test case 3: List with only odd numbers
    lista3 = [1, 3, 5, 7, 9]
    print(f"\nLista neparnih: {lista3}")
    print(f"Parni brojevi: {filtriraj_parne(lista3)}")

if __name__ == "__main__":
    main()