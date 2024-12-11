import asyncio

from aiohttp import ClientSession, web


async def fetch_cat_fact(session):
    async with session.get("https://catfact.ninja/fact") as response:
        return await response.json()


async def get_cat_facts(request):
    try:
        amount = int(request.match_info["amount"])
        if amount <= 0:
            return web.json_response({"error": "Amount must be positive"}, status=400)

        async with ClientSession() as session:
            tasks = [fetch_cat_fact(session) for _ in range(amount)]
            facts = await asyncio.gather(*tasks)
            facts_list = [fact["fact"] for fact in facts]

        return web.json_response({"facts": facts_list})
    except ValueError:
        return web.json_response({"error": "Invalid amount parameter"}, status=400)
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)


app = web.Application()
app.router.add_get("/cat/{amount}", get_cat_facts)
app.router.add_get("/cats", get_cat_facts)

if __name__ == "__main__":
    web.run_app(app, port=8086)
