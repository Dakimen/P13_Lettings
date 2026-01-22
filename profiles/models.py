"""
Define models for the profiles application.

This module provides model configuration for the profiles application.

Classes
-------
Profile
    Represents a user's profile.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a specific renter's profile.

    Attributes
    ----------
    user : User
        User associated with this profile.
    favorite_city : str
        This profile's favorite city, Ex: 'Anaheim'.

    Methods
    -------
    __str__():
        Returns profile's associated user's username.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns profile's associated user's username.
        """
        return self.user.username
