from datetime import datetime
from decimal import Decimal

import pytest

from models import Admin, CCTV_frame, Izdavac, Jelo, Knjiga, RestaurantOrder


def test_izdavac():
    izdavac = Izdavac(naziv="Znanje", adresa="Zagreb")
    assert izdavac.naziv == "Znanje"
    assert izdavac.adresa == "Zagreb"


def test_knjiga():
    izdavac = Izdavac(naziv="Znanje", adresa="Zagreb")
    knjiga = Knjiga(
        naslov="Python Programming",
        ime_autora="John",
        prezime_autora="Doe",
        broj_stranica=200,
        izdavac=izdavac,
    )
    assert knjiga.naslov == "Python Programming"
    assert knjiga.godina_izdavanja == datetime.now().year


def test_admin():
    admin = Admin(
        ime="Ana", prezime="Anić", korisnicko_ime="aanic", email="ana@test.com"
    )
    assert admin.ovlasti == []

    admin_with_permissions = Admin(
        ime="Ivan",
        prezime="Ivić",
        korisnicko_ime="iivic",
        email="ivan@test.com",
        ovlasti=["čitanje", "dodavanje"],
    )
    assert len(admin_with_permissions.ovlasti) == 2


def test_restaurant_order():
    jelo1 = Jelo(id=1, naziv="Pizza", cijena=70.0)
    jelo2 = Jelo(id=2, naziv="Salata", cijena=30.0)

    order = RestaurantOrder(
        id=1,
        ime_kupca="Marko",
        stol_info={"broj": 5, "lokacija": "terasa"},
        jela=[jelo1, jelo2],
        ukupna_cijena=100.0,
    )
    assert len(order.jela) == 2
    assert order.stol_info["lokacija"] == "terasa"


def test_cctv_frame():
    frame = CCTV_frame(id=1, vrijeme_snimanja=datetime.now())
    assert frame.koordinate == (Decimal("0.0"), Decimal("0.0"))

    frame_with_coords = CCTV_frame(
        id=2,
        vrijeme_snimanja=datetime.now(),
        koordinate=(Decimal("45.32"), Decimal("16.78")),
    )
    assert frame_with_coords.koordinate[0] == Decimal("45.32")


def test_invalid_data():
    with pytest.raises(ValueError):
        Knjiga(
            naslov="Python Programming",
            ime_autora="John",
            prezime_autora="Doe",
            broj_stranica=-1,
            izdavac={"naziv": "Znanje"},
        )

    with pytest.raises(ValueError):
        Admin(
            ime="Ana",
            prezime="Anić",
            korisnicko_ime="aanic",
            email="invalid-email",
            ovlasti=["invalid"],
        )
