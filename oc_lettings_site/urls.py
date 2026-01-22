"""
URL configuration for the oc_lettings_site application.

This module maps URL paths to the global-level views.

Variables
---------
urlpatterns : list
    List of URL patterns, mapping the index and admin pages, as well as including paths
    in lettings and profiles routers.
handler404 : str
    Path to the view displaying the not found page.
handler500 : str
    Path to the view displaying the internal server error page.
"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'oc_lettings_site.views.not_found'
handler500 = 'oc_lettings_site.views.internal_server_error'
