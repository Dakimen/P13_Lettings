import pytest

from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profiles_index(client):
    user = User.objects.create(username="Test_Dummy")
    Profile.objects.create(user=user, favorite_city="Anaheim")
    user2 = User.objects.create(username="Test_Dummy 2")
    Profile.objects.create(user=user2, favorite_city="Sacramento")
    url = reverse('profiles:index')
    response = client.get(url)
    content = response.content.decode()
    assert "Test_Dummy" in content
    assert "Test_Dummy 2" in content
    assert response.status_code == 200
    assert "profiles/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profile(client):
    user = User.objects.create(username="Test_Dummy", first_name="Michael",
                               last_name="Local", email="email@email.com")
    Profile.objects.create(user=user, favorite_city="Anaheim")
    url = reverse('profiles:profile', args=[user.username])
    response = client.get(url)
    content = response.content.decode()
    assert response.status_code == 200
    assert "Test_Dummy" in content
    assert "Michael" in content
    assert "Local" in content
    assert "email@email.com" in content
    assert "Anaheim" in content
    assert "profiles/profile.html" in [t.name for t in response.templates]
