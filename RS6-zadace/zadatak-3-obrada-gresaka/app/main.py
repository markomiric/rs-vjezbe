from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query

from app.models import Car, CarInput, CarOutput

app = FastAPI()

cars = {
    1: Car(
        id=1,
        marka="Toyota",
        model="Corolla",
        godina_proizvodnje=2020,
        cijena=25000.00,
        boja="silver",
    ),
    2: Car(
        id=2,
        marka="BMW",
        model="X5",
        godina_proizvodnje=2021,
        cijena=65000.00,
        boja="black",
    ),
}


@app.get("/cars/{car_id}", response_model=Car)
async def get_car(car_id: int):
    if car_id not in cars:
        raise HTTPException(status_code=404, detail="Automobil nije pronađen")
    return cars[car_id]


@app.get("/cars/", response_model=List[Car])
async def get_cars(
    min_cijena: Optional[float] = Query(None, gt=0),
    max_cijena: Optional[float] = None,
    min_godina: Optional[int] = Query(None, gt=1960),
    max_godina: Optional[int] = None,
):
    if min_cijena and max_cijena and min_cijena > max_cijena:
        raise HTTPException(
            status_code=400,
            detail="Minimalna cijena ne može biti veća od maksimalne cijene",
        )

    if min_godina and max_godina and min_godina > max_godina:
        raise HTTPException(
            status_code=400,
            detail="Minimalna godina ne može biti veća od maksimalne godine",
        )

    filtered_cars = cars.values()

    if min_cijena:
        filtered_cars = [car for car in filtered_cars if car.cijena >= min_cijena]
    if max_cijena:
        filtered_cars = [car for car in filtered_cars if car.cijena <= max_cijena]
    if min_godina:
        filtered_cars = [
            car for car in filtered_cars if car.godina_proizvodnje >= min_godina
        ]
    if max_godina:
        filtered_cars = [
            car for car in filtered_cars if car.godina_proizvodnje <= max_godina
        ]

    return filtered_cars


@app.post("/cars/", response_model=CarOutput)
async def create_car(car: CarInput):
    for existing_car in cars.values():
        if (
            existing_car.marka == car.marka
            and existing_car.model == car.model
            and existing_car.godina_proizvodnje == car.godina_proizvodnje
        ):
            raise HTTPException(status_code=400, detail="Automobil već postoji u bazi")

    new_id = max(cars.keys()) + 1 if cars else 1

    cijena_pdv = car.cijena * 1.25

    new_car = CarOutput(**car.model_dump(), id=new_id, cijena_pdv=cijena_pdv)

    cars[new_id] = new_car
    return new_car
