def obrni_rjecnik(rjecnik):
    return {vrijednost: kljuc for kljuc, vrijednost in rjecnik.items()}

def test_obrni_rjecnik():
    # Test 1: Basic dictionary
    rjecnik1 = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
    print("Test 1 - Osnovni rječnik:")
    print(f"Ulaz: {rjecnik1}")
    print(f"Rezultat: {obrni_rjecnik(rjecnik1)}\n")
    
    # Test 2: Empty dictionary
    rjecnik2 = {}
    print("Test 2 - Prazan rječnik:")
    print(f"Ulaz: {rjecnik2}")
    print(f"Rezultat: {obrni_rjecnik(rjecnik2)}\n")
    
    # Test 3: Dictionary with numbers
    rjecnik3 = {1: "jedan", 2: "dva", 3: "tri"}
    print("Test 3 - Rječnik s brojevima:")
    print(f"Ulaz: {rjecnik3}")
    print(f"Rezultat: {obrni_rjecnik(rjecnik3)}\n")
    
    # Test 4: Dictionary with boolean values
    rjecnik4 = {"aktivan": True, "prijavljen": False}
    print("Test 4 - Rječnik s boolean vrijednostima:")
    print(f"Ulaz: {rjecnik4}")
    print(f"Rezultat: {obrni_rjecnik(rjecnik4)}")

if __name__ == "__main__":
    test_obrni_rjecnik()