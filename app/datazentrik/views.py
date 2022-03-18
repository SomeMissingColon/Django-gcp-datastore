"""
Main view functions for handling requests.
"""

from django.shortcuts import (
    render,
    redirect,
)
from django.http import Http404 
from google.cloud import ndb
from datazentrik.models import Redirect


def landing(request):
    """Render the landing page."""
    redirects = Redirect.query().fetch()

    return render(request, 'datazentrik/index.html', {'redirects': redirects})


def handle_redirect(request, slug):
    """Handle a redirect."""
    redirect_entity = ndb.Key(Redirect,slug).get()
    if not redirect_entity:
        raise Http404('The page might or might not exist in the future. It sure isn\'t here right now.')
    return redirect(redirect_entity.destination_url,permanent=True)