def isPrime(broj):
    if broj < 2:
        return False
    for i in range(2, int(broj ** 0.5) + 1):
        if broj % i == 0:
            return False
    return True

def primes_in_range(start, end):
    return [broj for broj in range(max(2, start), end + 1) if isPrime(broj)]

def test_prosti_brojevi():
    # Test isPrime
    print("Test isPrime:")
    test_brojevi = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for broj in test_brojevi:
        print(f"Je li {broj} prost? {isPrime(broj)}")
    print()
    
    # Test primes_in_range
    print("Test primes_in_range:")
    test_rasponi = [
        (1, 10),
        (10, 20),
        (1, 1),
        (90, 100)
    ]
    for start, end in test_rasponi:
        print(f"Prosti brojevi od {start} do {end}: {primes_in_range(start, end)}")

if __name__ == "__main__":
    test_prosti_brojevi()