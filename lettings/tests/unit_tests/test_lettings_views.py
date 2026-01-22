import pytest

from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_letting_index(client):
    address = Address.objects.create(
        number=55, street="Wintermist Street", city="Anaheim",
        state="CA", zip_code=92804, country_iso_code="USA"
    )
    address2 = Address.objects.create(
        number=66, street="Wintermist Street", city="Anaheim",
        state="CA", zip_code=92804, country_iso_code="USA"
    )
    Letting.objects.create(title="Cozy Abode", address=address)
    Letting.objects.create(title="Cozy 2", address=address2)
    url = reverse('lettings:index')
    response = client.get(url)
    content = response.content.decode()
    assert "Cozy Abode" in content
    assert "Cozy 2" in content
    assert response.status_code == 200
    assert "lettings/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_letting(client):
    address = Address.objects.create(
        number=55, street="Wintermist Street", city="Anaheim",
        state="CA", zip_code=92804, country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Cozy Abode", address=address)
    url = reverse('lettings:letting', args=[letting.id])
    response = client.get(url)
    content = response.content.decode()
    assert response.status_code == 200
    assert "Cozy Abode" in content
    assert "55 Wintermist Street" in content
    assert "Anaheim, CA 92804" in content
    assert "USA" in content
    assert "lettings/letting.html" in [t.name for t in response.templates]
