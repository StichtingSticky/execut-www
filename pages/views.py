from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import *
from core.models import *

def get_site(request):

    # Get the site from the hostname
    
    hostname = request.get_host()

    try:
        site = Site.objects.filter(domain=hostname).get()
    except Site.DoesNotExist:
        raise Http404("This exec(ut)-site does not exist")

    if not site.is_active:
        raise Http404("exec(ut) will launch shortly - stay tuned!")        

    return site

def view_page(request, slug=None):

    site = get_site(request)

    if slug is None:

        # We're grabbing the home page then.

        page = get_object_or_404(StaticPage, slug='home')

    else:

        # Just a regular page

        page = get_object_or_404(StaticPage, slug=slug)

    # Check if the page belongs to this site.

    if page not in site.pages.filter(pk=page.id):
        raise Http404("This page could not be found")

    # All clear. Ready to build the static page.

    # Include committee if this is the about page
    
    if slug == "about":

        commissioners = site.committee.commissioners.all().order_by('official_order')

    else:

        commissioners = None


    page_title = page.name

    context = {
        "page_title": page_title,
        "site": site,
        "page": page,
        "commissioners": commissioners
    }

    return render(request, "pages/view.html", context)