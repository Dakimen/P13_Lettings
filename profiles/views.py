"""
Views for the profiles application.

This module provides the views for the profiles app, including the
list and detail pages for existing profiles.

Functions
---------
index(request)
    Displays a list of all profiles.
profile(request, username)
    Displays the details for a specific profile identified by `username`.
"""
from django.http import Http404
from django.shortcuts import render
from profiles.models import Profile
import logging

logger = logging.getLogger(__name__)


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    Display a list of all profiles.

    Parameters
    ----------
    request : HttpRequest
        The incoming HTTP request.

    Returns
    -------
    HttpResponse
        Rendered template with all profiles.
    """
    logger.info("Accessed profile index")
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus, it.
# Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Display a specific profile.

    Parameters
    ----------
    request : HttpRequest
        The incoming HTTP request.
    username : str
        Username of the profile to display

    Returns
    -------
    HttpResponse
        Rendered template with the chosen profile's details.
    """
    logger.info("Accessed profile details")
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logger.warning("Profile not found", extra={"user__username": username})
        raise Http404("Letting does not exist")
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
