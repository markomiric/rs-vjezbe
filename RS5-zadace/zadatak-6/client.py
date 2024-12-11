import asyncio
import time

import aiohttp


async def fetch_greeting(url, port):
    async with aiohttp.ClientSession() as session:
        full_url = f"http://{url}:{port}/pozdrav"
        async with session.get(full_url) as response:
            return await response.json()


async def main():
    print("Sequential requests:")
    start_time = time.time()

    result1 = await fetch_greeting("localhost", 8081)
    print(f"Response from 8081: {result1}")

    result2 = await fetch_greeting("localhost", 8082)
    print(f"Response from 8082: {result2}")

    print(f"Sequential time: {time.time() - start_time:.2f} seconds")

    print("\nConcurrent requests:")
    start_time = time.time()

    results = await asyncio.gather(
        fetch_greeting("localhost", 8081), fetch_greeting("localhost", 8082)
    )

    print(f"Response from 8081: {results[0]}")
    print(f"Response from 8082: {results[1]}")
    print(f"Concurrent time: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())


#  python .\client.py
# Sequential requests:
# Response from 8081: {'message': 'Pozdrav nakon 3 sekunde'}
# Response from 8082: {'message': 'Pozdrav nakon 4 sekunde'}
# Sequential time: 7.06 seconds

# Concurrent requests:
# Response from 8081: {'message': 'Pozdrav nakon 3 sekunde'}
# Response from 8082: {'message': 'Pozdrav nakon 4 sekunde'}
# Concurrent time: 4.00 seconds
