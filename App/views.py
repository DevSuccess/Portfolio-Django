from django.shortcuts import get_object_or_404
from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    try:
        profile = models.Profile.objects.get(active=True)
    except:
        profile = None

    try:
        about = models.About.objects.get(active=True)
    except:
        about = None

    try:
        contact = models.Contact.objects.get(privilege=True)
    except:
        contact = None

    try:
        skills = models.Skill.objects.get(active=True)
    except:
        skills = None

    try:
        facts = models.Fact.objects.get(active=True)
    except:
        facts = None

    context = {
        'about': about,
        'profile': profile,
        'contact': contact,
        'facts': facts,
        'skills': skills,
    }
    return render(request, 'App/index.html', context)
