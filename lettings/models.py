"""
Define models for the lettings application.

This module provides model configuration for the lettings application.

Classes:
-------
Address:
    Represents a property's address
Letting:
    Represents a specific listing up for renting.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represent a property's address.

    Attributes
    ----------
    number : int
        property's number on the specific street, represented by an integer. Ex: 200.
    street : str
        name of the street it is located on. Ex: 'Wintermist Street'.
    city : str
        name of the city. Ex: 'Anaheim'.
    state : str
        two letters representing state code. Ex: 'CA' for California.
    zip_code : int
        property's zip-code represented as a positive integer. Ex: 92804.
    country_iso_code : str
        country's three letter iso code. Ex: 'USA' for the United States of America.

    Methods
    -------
    __str__():
        Returns 'number street', e.g., '55 Wintermist Street'.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """
        Model metadata for Address.

        Specifies human-readable plural for admin interface.
        """
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Returns 'number street', e.g., '55 Wintermist Street'.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represent a specific listing up for renting.

    Attributes
    ----------
    title : str
        Listing's name. Ex: 'Cozy abode'.
    address : Address class instance
        Address instance for the property being listed.

    Methods
    -------
    __str__():
        Returns letting's title.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Returns letting's title."""
        return self.title
