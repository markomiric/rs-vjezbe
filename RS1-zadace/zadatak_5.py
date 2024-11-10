def faktorijel_while(n):
    if n < 0:
        return "Nije moguće izračunati faktorijel negativnog broja"
    rezultat = 1
    i = 1
    while i <= n:
        rezultat *= i
        i += 1
    return rezultat

def faktorijel_for(n):
    if n < 0:
        return "Nije moguće izračunati faktorijel negativnog broja"
    rezultat = 1
    for i in range(1, n + 1):
        rezultat *= i
    return rezultat

broj = int(input("Unesite broj za izračun faktorijela: "))

print(f"Faktorijel (while petlja): {faktorijel_while(broj)}")
print(f"Faktorijel (for petlja): {faktorijel_for(broj)}")