import asyncio

async def fetch_data():
    numbers = [x for x in range(1, 11)]
    await asyncio.sleep(3)
    
    print("Podaci dohvaćeni.")
    return numbers

async def main():
    await fetch_data()

if __name__ == "__main__":
    asyncio.run(main())