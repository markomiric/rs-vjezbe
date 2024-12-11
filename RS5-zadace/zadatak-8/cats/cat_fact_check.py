from aiohttp import web


async def check_facts(request):
    try:
        data = await request.json()
        if not isinstance(data.get("facts"), list):
            return web.json_response(
                {"error": "Input must contain 'facts' list"}, status=400
            )

        filtered_facts = [
            fact
            for fact in data["facts"]
            if "cat" in fact.lower() or "cats" in fact.lower()
        ]

        return web.json_response({"filtered_facts": filtered_facts})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)


app = web.Application()
app.router.add_post("/facts", check_facts)

if __name__ == "__main__":
    web.run_app(app, port=8087)
