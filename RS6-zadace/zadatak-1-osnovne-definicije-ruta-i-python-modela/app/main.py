from typing import List, Optional

from fastapi import FastAPI, HTTPException

from app.models import CreateFilm, Film

app = FastAPI()

filmovi: List[Film] = [
    Film(id=1, naziv="Titanic", genre="drama", godina=1997),
    Film(id=2, naziv="Inception", genre="akcija", godina=2010),
    Film(id=3, naziv="The Shawshank Redemption", genre="drama", godina=1994),
    Film(id=4, naziv="The Dark Knight", genre="akcija", godina=2008),
]


@app.get("/filmovi", response_model=List[Film])
def get_filmovi(genre: Optional[str] = None, min_godina: int = 2000) -> List[Film]:
    filtered_films = filmovi

    if genre:
        filtered_films = [f for f in filtered_films if f.genre == genre]

    filtered_films = [f for f in filtered_films if f.godina >= min_godina]

    return filtered_films


@app.get("/filmovi/{id}", response_model=Film)
def get_film_by_id(id: int) -> Film:
    for film in filmovi:
        if film.id == id:
            return film
    raise HTTPException(status_code=404, detail=f"Film with id {id} not found")


@app.post("/filmovi", response_model=Film)
def create_film(film: CreateFilm) -> Film:
    new_id = max(f.id for f in filmovi) + 1
    new_film = Film(id=new_id, **film.dict())
    filmovi.append(new_film)
    return new_film
