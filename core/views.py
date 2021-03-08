from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import *
from pages.models import *
from pages.views import get_site

def speakers(request):

    site = get_site(request)

    # Grab the speakers for this committee

    speakers = site.committee.speakers.all()

    page_title = "Speakers"

    # Ready to build the page

    context = {
        "page_title": page_title,
        "site": site,
        "speakers": speakers
    }

    return render(request, "speakers/all.html", context)

def single_speaker(request, speaker_id, speaker_slug):

    site = get_site(request)

    # Grab the current speaker

    speaker = get_object_or_404(Speaker, pk=speaker_id)

    page_title = speaker

    # Ready to build the page

    context = {
        "page_title": page_title,
        "site": site,
        "speaker": speaker
    }

    return render(request, "speakers/single_speaker.html", context)

def programme(request):

    site = get_site(request)

    # Very simple. Just grab all the activities and build the page.

    activities = Activity.objects.filter(committee=site.committee).order_by('commences_at')

    page_title = "Programme"

    context = {
        "page_title": page_title,
        "site": site,
        "activities": activities
    }

    return render(request, "programme/view.html", context)

def sponsors(request):

    site = get_site(request)

    # Grab the sponsors for this committee

    # First, grab the different kind of sponsorships

    sponsors = []

    for tier in SponsorshipTier.objects.all().order_by('order'):
        tier_entry = {}
        tier_entry['name'] = tier.name
        tier_entry['sponsors'] = []

        # Add in the sponsors for this tier and committee

        for sponsor in site.committee.sponsors.filter(sponsorship_kind=tier):
            tier_entry['sponsors'].append(sponsor)

        sponsors.append(tier_entry)

    page_title = "Partners"

    # Ready to build the page

    context = {
        "page_title": page_title,
        "site": site,
        "sponsors": sponsors
    }

    return render(request, "sponsors/all.html", context)

