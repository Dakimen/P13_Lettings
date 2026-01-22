import pytest

from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_str():
    user = User(username='Test_Dummy')
    profile = Profile(user=user, favorite_city="Anaheim")
    assert str(profile) == "Test_Dummy"
