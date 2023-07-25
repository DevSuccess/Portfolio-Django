from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    try:
        profile = models.Profile.objects.get(active=True)
    except:
        profile = None

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
        about_section = models.Section.objects.get(type__value__iexact='about')
    except:
        about_section = None

    try:
        skills_section = models.Section.objects.get(type__value__iexact='skills')
    except:
        skills_section = None

    try:
        facts_section = models.Section.objects.get(type__value__iexact='about')
    except:
        facts_section = None

    try:
        resume_section = models.Section.objects.get(type__value__iexact='resume')
    except:
        resume_section = None

    try:
        portfolio_section = models.Section.objects.get(type__value__iexact='portfolio')
    except:
        portfolio_section = None

    sommaries = models.Summary.objects.all()
    educations = models.Education.objects.all()
    experiences = models.Experience.objects.all()
    portfolios = models.Portfolio.objects.all()
    categories = models.CategoryPortfolio.objects.all()

    context = {
        'about_section': about_section,
        'facts_section': facts_section,
        'skills_section': skills_section,
        'resume_section': resume_section,
        'portfolio_section': portfolio_section,

        'profile': profile,
        'portfolios': portfolios,
        'categories': categories,
        'facts': facts,
        'contact': contact,
        'skills': skills,
        'sommaries': sommaries,
        'educations': educations,
        'experiences': experiences,
    }
    return render(request, 'App/index.html', context)
