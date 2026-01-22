import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_index_url(client):
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_detail_url(client):
    addr = Address.objects.create(number=1, street="Main", city="City",
                                  state="ST", zip_code=12345,
                                  country_iso_code="USA")
    letting = Letting.objects.create(title="Test", address=addr)
    url = reverse('lettings:letting', args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
