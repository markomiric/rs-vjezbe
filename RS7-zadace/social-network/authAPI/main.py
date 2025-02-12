import hashlib

from aiohttp import web

korisnici = [
    {
        "korisnicko_ime": "admin",
        "lozinka_hash": "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b",
    },  # lozinka = "lozinka123"
    {
        "korisnicko_ime": "markoMaric",
        "lozinka_hash": "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa",
    },  # lozinka = "markoKralj123"
    {
        "korisnicko_ime": "ivanHorvat",
        "lozinka_hash": "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302",
    },  # lozinka = "lllllllllllozinka_123"
    {
        "korisnicko_ime": "Nada000",
        "lozinka_hash": "492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d",
    },  # lozinka = "blablabla"
]


def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


async def register(request):
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "Invalid JSON"}, status=400)

    username = data.get("korisnicko_ime")
    password = data.get("lozinka")

    if not username or not password:
        return web.json_response({"error": "Missing username or password"}, status=400)

    if any(user["korisnicko_ime"] == username for user in korisnici):
        return web.json_response({"error": "Username already exists"}, status=400)

    new_user = {"korisnicko_ime": username, "lozinka_hash": hash_data(password)}
    korisnici.append(new_user)

    return web.json_response({"message": "Registration successful"}, status=201)


async def login(request):
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "Invalid JSON"}, status=400)

    username = data.get("korisnicko_ime")
    password = data.get("lozinka")

    if not username or not password:
        return web.json_response({"error": "Missing username or password"}, status=400)

    hashed_password = hash_data(password)
    for user in korisnici:
        if (
            user["korisnicko_ime"] == username
            and user["lozinka_hash"] == hashed_password
        ):
            return web.json_response({"result": True})

    return web.json_response({"result": False}, status=401)


async def health(request):
    return web.Response(text="AuthAPI is running.")


app = web.Application()
app.add_routes(
    [
        web.get("/", health),
        web.post("/login", login),
        web.post("/register", register),
    ]
)

if __name__ == "__main__":
    web.run_app(app, port=9000)
