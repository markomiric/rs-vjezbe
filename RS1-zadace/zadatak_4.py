print("Prvi primjer:")
broj = 0
while broj < 5:
    broj += 2
    print(broj)
# Ovo će ispisati: 2, 4, 6 (izlazi nakon 6 jer je 6 >= 5)

print("\nDrugi primjer (zakomentiran jer je beskonačan):")
# broj = 0
# while broj < 5:
#     broj += 1
#     print(broj)
#     broj -= 1
# Ovo je beskonačno jer je broj uvijek < 5 (dodaje 1, ispisuje, zatim oduzima 1)

print("\nTreći primjer:")
broj = 10
while broj > 0:
    broj -= 1
    print(broj)
    if broj < 5:
        broj += 2
# Problem: "if" unutar petlje može uzrokovati ponavljanje brojeva

print("\nPrimjer for petlje:")
for i in range(1, 11):
    print(f"Broj: {i}")

print("\nTablica množenja:")
for redak in range(1, 11):
    ispisRetka = ""
    for stupac in range(1, 11):
        umnozak = redak * stupac
        ispisRetka += f"{umnozak:4}"
    print(ispisRetka)