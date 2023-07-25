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
    try:
        resume = models.Resume.objects.get(active=True)
    except:
        resume = None

    sommaries = models.Summary.objects.all()
    educations = models.Education.objects.all()
    experiences = models.Experience.objects.all()

    context = {
        'about': about,
        'profile': profile,
        'contact': contact,
        'facts': facts,
        'skills': skills,
        'resume': resume,
        'sommaries': sommaries,
        'educations': educations,
        'experiences': experiences,
    }
    return render(request, 'App/index.html', context)
