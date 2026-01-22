"""
Application configuration for the oc_lettings_site app.

This app serves as a base app, allowing navigation to other existings apps.
It also provides urls and views for administration, home page and error pages.
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """Configuration class for the oc_lettings_site Django application."""
    name = 'oc_lettings_site'
