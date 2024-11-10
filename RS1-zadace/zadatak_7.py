def provjera_lozinke(lozinka):
    if not (8 <= len(lozinka) <= 15):
        return "Lozinka mora sadržavati između 8 i 15 znakova"
    
    has_upper = any(c.isupper() for c in lozinka)
    has_digit = any(c.isdigit() for c in lozinka)
    if not (has_upper and has_digit):
        return "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj"
    
    lozinka_lower = lozinka.lower()
    if "password" in lozinka_lower or "lozinka" in lozinka_lower:
        return "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'"
    
    return "Lozinka je jaka!"

def main():
    lozinka = input("Unesite lozinku: ")
    rezultat = provjera_lozinke(lozinka)
    print(rezultat)

if __name__ == "__main__":
    main()