"""
Views for the lettings application.

This module provides the views for the lettings app, including the
list and detail pages for property listings.

Functions
---------
index(request)
    Displays a list of all lettings.
letting(request, letting_id)
    Displays the details for a specific letting identified by `letting_id`.
"""
from django.shortcuts import render
from django.http import Http404
from lettings.models import Letting
import logging

logger = logging.getLogger(__name__)


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat
# massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices
# posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Display a list of all lettings.

    Parameters
    ----------
    request : HttpRequest
        The incoming HTTP request.

    Returns
    -------
    HttpResponse
        Rendered template with all lettings.
    """
    logger.info("Accessed lettings index")
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu,
# vitae efficitur
# lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est ut luctus
# congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo mattis
# ullamcorper ac non tellus. In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus. Mauris condimentum
# auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim,
# ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    Display a specific lettings.

    Parameters
    ----------
    request : HttpRequest
        The incoming HTTP request.
    letting_id : int
        Id of the letting to display.

    Returns
    -------
    HttpResponse
        Rendered template with title and address of the letting.
    """
    logger.info("Accessed letting detail view", extra={"letting_id": letting_id})
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.warning("Letting not found", extra={"letting_id": letting_id})
        raise Http404("Letting does not exist")
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
