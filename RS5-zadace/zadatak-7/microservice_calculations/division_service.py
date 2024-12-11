from aiohttp import web


async def handle_division(request):
    try:
        data = await request.json()
        sum_result = data["sum"]
        multiplication_result = data["multiplication"]

        if sum_result == 0:
            return web.json_response({"error": "Cannot divide by zero"}, status=400)

        result = multiplication_result / sum_result
        return web.json_response({"result": result})
    except Exception:
        return web.json_response({"error": "Invalid input format"}, status=400)


app = web.Application()
app.router.add_post("/kolicnik", handle_division)

if __name__ == "__main__":
    web.run_app(app, port=8085)
