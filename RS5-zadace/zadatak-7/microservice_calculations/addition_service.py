from aiohttp import web


async def handle_sum(request):
    try:
        data = await request.json()
        if not isinstance(data, list) or not data:
            return web.json_response(
                {"error": "Input must be a non-empty list of numbers"}, status=400
            )
        result = sum(data)
        return web.json_response({"result": result})
    except Exception:
        return web.json_response({"error": "Invalid input format"}, status=400)


app = web.Application()
app.router.add_post("/zbroj", handle_sum)

if __name__ == "__main__":
    web.run_app(app, port=8083)
