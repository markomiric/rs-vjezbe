import asyncio
import aiohttp
import time

async def fetch_users():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/users') as response:
            return await response.json()

async def main():
    start_time = time.time()
    
    tasks = [fetch_users() for _ in range(5)]
    results = await asyncio.gather(*tasks)
    
    users = results[0]
    
    names = [user['name'] for user in users]
    emails = [user['email'] for user in users]
    usernames = [user['username'] for user in users]
    
    print("\nKorisnička imena:")
    print(usernames)
    print("\nEmail adrese:")
    print(emails)
    print("\nImena:")
    print(names)
    
    end_time = time.time()
    print(f"\nVrijeme izvršavanja: {end_time - start_time:.2f} sekundi")

if __name__ == "__main__":
    asyncio.run(main())