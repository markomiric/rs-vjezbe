print("1. Loop with range(1, 2):")
for i in range(1, 2):
    print(i)
print("Ova petlja nema smisla jer se izvršava samo jednom\n")

print("2. Loop with range(1, 10, 2):")
for i in range(1, 10, 2):
    print(i, end=" ")
print("\nIspisuje neparne brojeve od 1 do 9\n")

print("3. Loop with range(10, 1, -1):")
for i in range(10, 1, -1):
    print(i, end=" ")
print("\nIspisuje brojeve od 10 do 2 silazno")