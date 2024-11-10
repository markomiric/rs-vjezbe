broj1 = float(input("Unesite prvi broj: "))
broj2 = float(input("Unesite drugi broj: "))
operator = input("Unesite operator (+, -, *, /): ")

valid_operators = ['+', '-', '*', '/']

if operator not in valid_operators:
    print("Nepodržani operator!")
else:
    try:
        if operator == '+':
            rezultat = broj1 + broj2
        elif operator == '-':
            rezultat = broj1 - broj2
        elif operator == '*':
            rezultat = broj1 * broj2
        else:
            if broj2 == 0:
                print("Dijeljenje s nulom nije dozvoljeno!")
                exit()
            rezultat = broj1 / broj2
        
        print(f"Rezultat operacije {broj1} {operator} {broj2} je {rezultat}")
            
    except Exception:
        print("Došlo je do greške!")