import re
from enum import Enum
from typing import List, Literal, Optional

from pydantic import BaseModel, HttpUrl, field_validator


class ContentType(str, Enum):
    MOVIE = "movie"
    SERIES = "series"


class Actor(BaseModel):
    """Defines a single actor with name and surname."""

    name: str
    surname: str


class Writer(BaseModel):
    """Defines a single writer with name and surname."""

    name: str
    surname: str


class Movie(BaseModel):
    Title: str
    Year: str
    Rated: str
    Runtime: str
    Genre: str
    Language: str
    Country: str
    Actors: str
    Plot: str
    Writer: str

    ComingSoon: Optional[bool] = None
    Director: Optional[str] = None
    Awards: Optional[str] = None
    Poster: Optional[str] = None
    Metascore: Optional[str] = None
    imdbRating: Optional[float] = None
    imdbVotes: Optional[int] = None
    imdbID: Optional[str] = None
    Type: Optional[Literal["movie", "series"]] = None
    totalSeasons: Optional[str] = None
    Response: Optional[str] = None
    Images: Optional[List[HttpUrl]] = None

    @field_validator("Year", mode="before")
    def validate_year(cls, value):
        """
        Accept strings like "2009" or "2011–" or "2013–2018".
        Extract the first 4-digit number, parse as int,
        then ensure it's > 1900.
        """
        match = re.search(r"\d{4}", value)
        if not match:
            raise ValueError(f"Cannot find a valid four-digit year in '{value}'")

        year_int = int(match.group(0))
        if year_int <= 1900:
            raise ValueError(f"Year must be greater than 1900; got {year_int}")

        return "".join(filter(str.isdigit, value[:4]))

    @field_validator("Runtime")
    def validate_runtime(cls, value):
        """
        If runtime is "N/A", leave as "N/A".
        Otherwise, parse the numeric part.
        """
        if value.strip().upper() == "N/A":
            return value

        match = re.match(r"(\d+)", value)
        if not match:
            raise ValueError("Runtime must contain a numeric value (e.g., '162 min').")
        minutes = int(match.group(1))
        if minutes <= 0:
            raise ValueError("Runtime must be greater than 0.")
        return value

    @field_validator("imdbRating", mode="before")
    def parse_imdb_rating(cls, value):
        """
        Convert "N/A" to None.
        Otherwise, convert string to float.
        """
        if value is None:
            return None
        if str(value).strip().upper() == "N/A":
            return None
        try:
            rating = float(value)
        except ValueError:
            raise ValueError("imdbRating must be a valid number.")
        return rating

    @field_validator("imdbRating")
    def validate_imdb_rating_range(cls, value):
        """
        Ensure imdbRating is between 0 and 10 if not None.
        """
        if value is not None and not (0 <= value <= 10):
            raise ValueError("imdbRating must be between 0 and 10.")
        return value

    @field_validator("imdbVotes", mode="before")
    def parse_imdb_votes(cls, value):
        """
        Convert "N/A" to None or parse integer (remove commas).
        """
        if value is None:
            return None
        if str(value).strip().upper() == "N/A":
            return None

        no_commas = value.replace(",", "")
        try:
            votes = int(no_commas)
        except ValueError:
            raise ValueError("imdbVotes must be an integer (e.g., '890,617').")
        return votes

    @field_validator("imdbVotes")
    def validate_imdb_votes_positive(cls, value):
        """
        Ensure imdbVotes > 0 if not None.
        """
        if value is not None and value <= 0:
            raise ValueError("imdbVotes must be greater than 0.")
        return value

    @field_validator("Images")
    def validate_images(cls, value):
        """
        Images is declared as List[HttpUrl], so each item must be a valid URL.
        If you need to enforce HTTPS or other specifics, you could do so here.
        """
        return value

    @field_validator("Type")
    def validate_type(cls, value):
        """
        If provided, Type must be either 'movie' or 'series' (handled by Literal).
        This validator ensures a clearer error message if needed.
        """
        return value
