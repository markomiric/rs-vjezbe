import aiohttp
from aiohttp import web

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50},
]

narudzbe = []


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


async def create_narudzba(request):
    data = await request.json()
    proizvod_id = data.get("proizvod_id")
    kolicina = data.get("kolicina")

    proizvod = next((p for p in proizvodi if p["id"] == proizvod_id), None)
    if proizvod is None:
        return web.json_response(
            {"error": "Proizvod s traženim ID-em ne postoji"}, status=404
        )

    nova_narudzba = {
        "id": len(narudzbe) + 1,
        "proizvod_id": proizvod_id,
        "kolicina": kolicina,
    }
    narudzbe.append(nova_narudzba)

    return web.json_response(narudzbe, status=201)


async def main():
    app = web.Application()
    app.router.add_get("/proizvodi", get_proizvodi)
    app.router.add_get("/proizvodi/{id}", get_proizvod)
    app.router.add_post("/narudzbe", create_narudzba)

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
            print("Nepostojeći proizvod:", await resp.json())

        order_data = {"proizvod_id": 1, "kolicina": 2}
        async with session.post(
            "http://localhost:8081/narudzbe", json=order_data
        ) as resp:
            print("Nova narudzba:", await resp.json())

        invalid_order = {"proizvod_id": 999, "kolicina": 1}
        async with session.post(
            "http://localhost:8081/narudzbe", json=invalid_order
        ) as resp:
            print("Nepostojeća narudzba:", await resp.json())

    await runner.cleanup()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
