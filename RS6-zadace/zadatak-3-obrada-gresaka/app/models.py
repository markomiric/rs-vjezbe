from pydantic import BaseModel


class Car(BaseModel):
    id: int
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str


class BaseCar(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str


class CarInput(BaseCar):
    pass


class CarOutput(BaseCar):
    id: int
    cijena_pdv: float
