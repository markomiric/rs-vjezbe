def brojanje_riječi(tekst):
    riječi = tekst.split()
    brojač = {}
    
    for riječ in riječi:
        if riječ in brojač:
            brojač[riječ] += 1
        else:
            brojač[riječ] = 1
            
    return brojač

def test_brojanje_riječi():
    # Test 1: Given example
    tekst1 = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
    print("Test 1 - Primjer teksta:")
    print(f"Tekst: {tekst1}")
    print(f"Rezultat: {brojanje_riječi(tekst1)}\n")
    
    # Test 2: Empty text
    tekst2 = ""
    print("Test 2 - Prazan tekst:")
    print(f"Tekst: '{tekst2}'")
    print(f"Rezultat: {brojanje_riječi(tekst2)}\n")
    
    # Test 3: Single word repeated
    tekst3 = "test test test test"
    print("Test 3 - Ponavljanje jedne riječi:")
    print(f"Tekst: {tekst3}")
    print(f"Rezultat: {brojanje_riječi(tekst3)}")

if __name__ == "__main__":
    test_brojanje_riječi()