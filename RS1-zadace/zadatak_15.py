def count_vowels_consonants(tekst):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    
    return {
        'vowels': sum(1 for c in tekst if c in vowels),
        'consonants': sum(1 for c in tekst if c in consonants)
    }

def test_count_vowels_consonants():
    tekst1 = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
    print("Test 1 - Primjer teksta:")
    print(f"Tekst: {tekst1}")
    print(f"Rezultat: {count_vowels_consonants(tekst1)}\n")
    
    tekst2 = ""
    print("Test 2 - Prazan tekst:")
    print(f"Tekst: '{tekst2}'")
    print(f"Rezultat: {count_vowels_consonants(tekst2)}\n")
    
    tekst3 = "aeiouAEIOU"
    print("Test 3 - Samo samoglasnici:")
    print(f"Tekst: {tekst3}")
    print(f"Rezultat: {count_vowels_consonants(tekst3)}\n")
    
    tekst4 = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    print("Test 4 - Samo suglasnici:")
    print(f"Tekst: {tekst4}")
    print(f"Rezultat: {count_vowels_consonants(tekst4)}")

if __name__ == "__main__":
    test_count_vowels_consonants()