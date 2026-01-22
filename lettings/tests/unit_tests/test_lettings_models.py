from lettings.models import Address, Letting


def test_address_str():
    addr = Address(number=55, street="Wintermist Street", city="Anaheim",
                   state="CA", zip_code=92804, country_iso_code="USA")
    assert str(addr) == "55 Wintermist Street"


def test_letting_str():
    addr = Address(number=55, street="Wintermist Street", city="Anaheim",
                   state="CA", zip_code=92804, country_iso_code="USA")
    letting = Letting(title="Cozy Abode", address=addr)
    assert str(letting) == "Cozy Abode"
