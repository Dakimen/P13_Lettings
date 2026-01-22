import pytest

from django.test import override_settings, RequestFactory
from django.urls import reverse
from oc_lettings_site.views import internal_server_error


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    content = response.content.decode()
    expected = "Welcome to Holiday Homes"
    assert expected in content
    assert response.status_code == 200
    assert "index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
@override_settings(DEBUG=False)
def test_404_page(client):
    url = reverse('lettings:letting', args=[999999])
    response = client.get(url)

    content = response.content.decode()
    assert response.status_code == 404
    assert "Page not found!" in content


def test_500_view_renders_template():
    request = RequestFactory().get("/")
    response = internal_server_error(request)
    assert response.status_code == 500
    content = response.content.decode()
    assert "500" in content
