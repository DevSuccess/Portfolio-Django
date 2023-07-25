from itertools import count

from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    profiles = models.Profile.objects.all().first()
    abouts = models.About.objects.all().first()
    web = models.Web.objects.filter(type__iexact='Portfolio').first()
    contact = models.Contact.objects.filter(type__iexact='Contact').first()
    skills = models.Skill.objects.all().first()
    context = {
        'abouts': abouts,
        'profiles': profiles,
        'web': web,
        'contact': contact,
        'fact_happy': models.Contact.objects.all().count(),
        'fact_project': models.Web.objects.all().count(),
        'skills': skills,
    }
    return render(request, 'App/index.html', context)
