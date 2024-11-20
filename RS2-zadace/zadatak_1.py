# 1. Kvadriranje broja
kvadriraj = lambda x: x ** 2

# 2. Zbroji pa kvadriraj
zbroji_pa_kvadriraj = lambda a, b: (a + b) ** 2

# 3. Kvadriraj duljinu niza
kvadriraj_duljinu = lambda niz: len(niz) ** 2

# 4. Pomnoži vrijednost s 5 pa potenciraj na x
pomnozi_i_potenciraj = lambda x, y: (y * 5) ** x

# 5. Vrati True ako je broj paran, inače None
paran_broj = lambda x: True if x % 2 == 0 else None

def test_kvadriraj():
    print("Testing kvadriraj...")
    print(f"kvadriraj(2) = {kvadriraj(2)}, expected 4")
    print(f"kvadriraj(-3) = {kvadriraj(-3)}, expected 9")
    print(f"kvadriraj(0) = {kvadriraj(0)}, expected 0")

def test_zbroji_pa_kvadriraj():
    print("\nTesting zbroji_pa_kvadriraj...")
    print(f"zbroji_pa_kvadriraj(2,3) = {zbroji_pa_kvadriraj(2,3)}, expected 25")
    print(f"zbroji_pa_kvadriraj(-1,1) = {zbroji_pa_kvadriraj(-1,1)}, expected 0")
    print(f"zbroji_pa_kvadriraj(0,0) = {zbroji_pa_kvadriraj(0,0)}, expected 0")

def test_kvadriraj_duljinu():
    print("\nTesting kvadriraj_duljinu...")
    print(f"kvadriraj_duljinu('test') = {kvadriraj_duljinu('test')}, expected 16")
    print(f"kvadriraj_duljinu('') = {kvadriraj_duljinu('')}, expected 0")
    print(f"kvadriraj_duljinu('abc') = {kvadriraj_duljinu('abc')}, expected 9")

def test_pomnozi_i_potenciraj():
    print("\nTesting pomnozi_i_potenciraj...")
    print(f"pomnozi_i_potenciraj(2,3) = {pomnozi_i_potenciraj(2,3)}, expected 225")
    print(f"pomnozi_i_potenciraj(3,2) = {pomnozi_i_potenciraj(3,2)}, expected 1000")
    print(f"pomnozi_i_potenciraj(0,1) = {pomnozi_i_potenciraj(0,1)}, expected 1")

def test_paran_broj():
    print("\nTesting paran_broj...")
    print(f"paran_broj(2) = {paran_broj(2)}, expected True")
    print(f"paran_broj(3) = {paran_broj(3)}, expected None")
    print(f"paran_broj(0) = {paran_broj(0)}, expected True")

if __name__ == '__main__':
    test_kvadriraj()
    test_zbroji_pa_kvadriraj()
    test_kvadriraj_duljinu()
    test_pomnozi_i_potenciraj() 
    test_paran_broj()