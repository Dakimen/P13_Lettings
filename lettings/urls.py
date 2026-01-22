"""
URL configuration for the lettings application.

This module maps URL paths to the lettings views.

Variables
---------
app_name : str
    The namespace for the lettings URLs.
urlpatterns : list
    List of URL patterns, mapping the index and detail pages of lettings.
"""


from django.urls import path

from lettings import views

app_name = "lettings"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
