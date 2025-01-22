from pydantic import BaseModel


class CreateFilm(BaseModel):
    naziv: str
    genre: str
    godina: int


class Film(CreateFilm):
    id: int
