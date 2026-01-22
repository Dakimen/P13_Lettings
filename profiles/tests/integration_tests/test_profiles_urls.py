import pytest
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profiles_index_url(client):
    url = reverse('profiles:index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_detail_url(client):
    user = User.objects.create(username='Test_Dummy')
    Profile.objects.create(user=user, favorite_city="Anaheim")
    url = reverse('profiles:profile', args=[user.username])
    response = client.get(url)
    assert response.status_code == 200
