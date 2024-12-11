import asyncio

from aiohttp import web


async def handle_greeting(request):
    await asyncio.sleep(4)
    return web.json_response({"message": "Pozdrav nakon 4 sekunde"})


app = web.Application()
app.router.add_get("/pozdrav", handle_greeting)

if __name__ == "__main__":
    web.run_app(app, port=8082)
