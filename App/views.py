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

    context = {
        'about': about,
        'profile': profile,
        'contact': contact,
        'fact_happy': models.Contact.objects.all().count(),
        'fact_project': models.Web.objects.all().count(),
        'skills': skills,
    }
    return render(request, 'App/index.html', context)
