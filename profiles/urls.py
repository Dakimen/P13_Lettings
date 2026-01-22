"""
URL configuration for the profiles application.

This module maps URL paths to the profile views.

Variables
---------
app_name : str
    The namespace for the profiles URLs.
urlpatterns : list
    List of URL patterns, mapping the index and detail pages of profiles.
"""

from django.urls import path

from profiles import views

app_name = "profiles"

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
