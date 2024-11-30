import asyncio

async def fetch_users():
    users = [
        {"id": 1, "name": "Ana", "email": "ana@mail.com"},
        {"id": 2, "name": "Petar", "email": "petar@mail.com"},
        {"id": 3, "name": "Marko", "email": "marko@mail.com"}
    ]
    
    await asyncio.sleep(3)
    return users

async def fetch_products():
    products = [
        {"id": 1, "name": "Laptop", "price": 999},
        {"id": 2, "name": "Phone", "price": 599},
        {"id": 3, "name": "Tablet", "price": 299}
    ]
    
    await asyncio.sleep(5)
    return products

async def main():
    users_data, products_data = await asyncio.gather(
        fetch_users(),
        fetch_products()
    )
    
    print("\nDohvaćeni podaci o korisnicima:", users_data)
    print("\nDohvaćeni podaci o proizvodima:", products_data)

if __name__ == "__main__":
    asyncio.run(main())