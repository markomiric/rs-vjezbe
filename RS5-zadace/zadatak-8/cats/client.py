import asyncio

import aiohttp


async def get_cat_facts(session, amount):
    async with session.get(f"http://localhost:8086/cat/{amount}") as response:
        return await response.json()


async def filter_facts(session, facts):
    async with session.post("http://localhost:8087/facts", json=facts) as response:
        return await response.json()


async def main():
    amount = 5

    async with aiohttp.ClientSession() as session:
        print(f"Fetching {amount} cat facts...")
        facts_response = await get_cat_facts(session, amount)

        if "error" in facts_response:
            print(f"Error: {facts_response['error']}")
            return

        print("\nReceived facts:")
        for i, fact in enumerate(facts_response["facts"], 1):
            print(f"{i}. {fact}")

        print("\nFiltering facts containing 'cat' or 'cats'...")
        filtered_response = await filter_facts(session, facts_response)

        if "error" in filtered_response:
            print(f"Error: {filtered_response['error']}")
            return

        print("\nFiltered facts:")
        for i, fact in enumerate(filtered_response["filtered_facts"], 1):
            print(f"{i}. {fact}")


if __name__ == "__main__":
    asyncio.run(main())
