from aiohttp import web

# Definiranje liste proizvoda
proizvodi = [
    {"naziv": "Jabuka", "cijena": 3.5, "količina": 50},
    {"naziv": "Kruška", "cijena": 4.0, "količina": 30},
    {"naziv": "Banana", "cijena": 5.5, "količina": 20},
]


async def handle_get_proizvodi(request):
    return web.json_response(proizvodi)


app = web.Application()
app.router.add_get("/proizvodi", handle_get_proizvodi)

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=8081)
