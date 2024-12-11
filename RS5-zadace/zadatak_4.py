import aiohttp
from aiohttp import web

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50},
]


async def get_proizvodi(request):
    return web.json_response(proizvodi)


async def get_proizvod(request):
    proizvod_id = int(request.match_info["id"])
    proizvod = next((p for p in proizvodi if p["id"] == proizvod_id), None)

    if proizvod is None:
        return web.json_response(
            {"error": "Proizvod s traženim ID-em ne postoji"}, status=404
        )
    return web.json_response(proizvod)


async def main():
    app = web.Application()
    app.router.add_get("/proizvodi", get_proizvodi)
    app.router.add_get("/proizvodi/{id}", get_proizvod)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8081)
    await site.start()

    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8081/proizvodi") as resp:
            print("Svi proizvodi:", await resp.json())

        async with session.get("http://localhost:8081/proizvodi/1") as resp:
            print("Proizvod 1:", await resp.json())

        async with session.get("http://localhost:8081/proizvodi/999") as resp:
            print("Nepostojeći proizvi:", await resp.json())

    await runner.cleanup()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
