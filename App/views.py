from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    profiles = models.Profile.objects.all().first()
    context = {
        'profiles': profiles
    }
    return render(request, 'App/index.html', context)
