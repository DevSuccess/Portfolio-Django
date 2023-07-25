from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    profiles = models.Profile.objects.all().first()
    abouts = models.About.objects.all().first()
    web = models.Web.objects.filter(type__iexact='Portfolio').first()
    contact = models.Contact.objects.filter(type__iexact='Contact').first()
    context = {
        'abouts': abouts,
        'profiles': profiles,
        'web': web,
        'contact': contact
    }
    return render(request, 'App/index.html', context)
