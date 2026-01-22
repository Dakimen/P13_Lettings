"""
Views for the oc_lettings_site application.

This module provides the views for the oc_lettings_site, including
the home page and pages for 404 and 500 errors.

Functions
---------
index(request)
    Displays the home page.
not_found(request, exception)
    Displays the error 404 page.
internal_server_error(request)
    Displays the error 500 page.
"""

from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis,
# sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis
# enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Display the home page.

    Parameters
    ----------
    request : HttpRequest
        The incoming HTTP request.

    Returns
    -------
    HttpResponse
        Rendered home page template.
    """
    logger.info("Accessed home index")
    return render(request, 'index.html')


def not_found(request, exception=None):
    """
    Display the custom 404 error page.

    Parameters
    ----------
    request : HttpRequest
        The incoming HTTP request.
    exception : Exception, optional
        The exception that triggered the 404 error (default is None).

    Returns
    -------
    HttpResponse
        Rendered 404 error page template with status 404.
    """
    logger.warning("Page not found: %s", request.path)
    return render(request, '404.html', status=404)


def internal_server_error(request):
    """
    Display the custom 500 error page.

    Parameters
    ----------
    request : HttpRequest
        The incoming HTTP request.

    Returns
    -------
    HttpResponse
        Rendered 500 error page template with status 500.
    """
    logger.error("Internal server error at %s", request.path, exc_info=True)
    return render(request, '500.html', status=500)
