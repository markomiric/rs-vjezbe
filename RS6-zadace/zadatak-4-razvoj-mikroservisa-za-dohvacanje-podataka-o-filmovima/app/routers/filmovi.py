import json
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from ..models.movie import ContentType, Movie

router = APIRouter(prefix="/movies", tags=["movies"])


def load_movies():
    with open("data/Film.JSON", encoding="utf-8") as f:
        movies_data = json.load(f)
        return [Movie(**movie) for movie in movies_data]


movies = load_movies()


@router.get("/", response_model=List[Movie])
async def get_all_movies(
    min_year: Optional[int] = Query(None, ge=1900),
    max_year: Optional[int] = Query(None, le=2100),
    min_rating: Optional[float] = Query(None, ge=0, le=10),
    max_rating: Optional[float] = Query(None, ge=0, le=10),
    type: Optional[ContentType] = None,
):
    filtered_movies = movies.copy()

    if min_year:
        filtered_movies = [
            m for m in filtered_movies if m.Year and int(m.Year) >= min_year
        ]
    if max_year:
        filtered_movies = [
            m for m in filtered_movies if m.Year and int(m.Year) <= max_year
        ]
    if min_rating:
        filtered_movies = [
            m for m in filtered_movies if m.imdbRating and m.imdbRating >= min_rating
        ]
    if max_rating:
        filtered_movies = [
            m for m in filtered_movies if m.imdbRating and m.imdbRating <= max_rating
        ]
    if type:
        filtered_movies = [m for m in filtered_movies if m.Type == type]

    return filtered_movies


@router.get("/{imdb_id}", response_model=Movie)
async def get_movie_by_id(imdb_id: str):
    movie = next((m for m in movies if m.imdbID == imdb_id), None)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.get("/title/{title}", response_model=Movie)
async def get_movie_by_title(title: str):
    movie = next((m for m in movies if m.Title.lower() == title.lower()), None)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
