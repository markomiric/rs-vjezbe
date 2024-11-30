import asyncio

async def secure_data(data):
    await asyncio.sleep(3)
    
    encrypted_data = {
        'prezime': data['prezime'],
        'broj_kartice': 'enkriptirano',
        'CVV': 'enkriptirano'
    }
    
    encrypted_data['hash_kartice'] = hash(str(data['broj_kartice']))
    encrypted_data['hash_cvv'] = hash(str(data['CVV']))
    
    return encrypted_data

async def main():
    osjetljivi_podaci = [
        {'prezime': 'Horvat', 'broj_kartice': '4532-1234-5678-9012', 'CVV': '123'},
        {'prezime': 'Kovač', 'broj_kartice': '4532-9876-5432-1098', 'CVV': '456'},
        {'prezime': 'Babić', 'broj_kartice': '4532-4567-8901-2345', 'CVV': '789'}
    ]
    
    zadaci = [asyncio.create_task(secure_data(podatak)) for podatak in osjetljivi_podaci]
    
    rezultati = await asyncio.gather(*zadaci)
    
    for i, rezultat in enumerate(rezultati, 1):
        print(f"\nPodaci {i}:")
        print(rezultat)

if __name__ == "__main__":
    asyncio.run(main())