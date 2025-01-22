from fastapi import FastAPI

from .routers import filmovi

app = FastAPI(
    title="Movie API",
    description="A microservice for retrieving movie information",
    version="1.0.0",
)

app.include_router(filmovi.router)
