from datetime import datetime
from decimal import Decimal
from typing import List, Literal, Tuple, TypedDict

from pydantic import BaseModel


class Izdavac(BaseModel):
    naziv: str
    adresa: str


class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: int = datetime.now().year
    broj_stranica: int
    izdavac: Izdavac


Ovlasti = Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]


class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: List[Ovlasti] = []


class StolInfo(TypedDict):
    broj: int
    lokacija: str


class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float


class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info: StolInfo
    jela: List[Jelo]
    ukupna_cijena: float


class CCTV_frame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: Tuple[Decimal, Decimal] = (Decimal("0.0"), Decimal("0.0"))
