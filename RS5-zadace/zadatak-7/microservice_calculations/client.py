import asyncio

import aiohttp


async def call_service(session, url, data):
    async with session.post(url, json=data) as response:
        return await response.json()


async def main():
    numbers = [1, 2, 3, 4, 5]

    async with aiohttp.ClientSession() as session:
        sum_task = call_service(session, "http://localhost:8083/zbroj", numbers)
        mult_task = call_service(session, "http://localhost:8084/umnozak", numbers)

        results = await asyncio.gather(sum_task, mult_task)
        sum_result = results[0]["result"]
        mult_result = results[1]["result"]

        print(f"Sum result: {sum_result}")
        print(f"Multiplication result: {mult_result}")

        division_data = {"sum": sum_result, "multiplication": mult_result}

        division_result = await call_service(
            session, "http://localhost:8085/kolicnik", division_data
        )

        print(f"Division result: {division_result['result']}")


if __name__ == "__main__":
    asyncio.run(main())


#  python client.py
# Sum result: 15
# Multiplication result: 120
# Division result: 8.0
