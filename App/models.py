from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe

from Web.utils import BaseModel, ImageModel, STATES, SOCIALS


# Create your models here.
class Localisation(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    lot = models.CharField(max_length=15)
    state = models.CharField(max_length=250, choices=STATES)
    zip_code = models.CharField(max_length=10)
    map = models.TextField(blank=True)

    def admin_map(self):
        return mark_safe(f"{self.map}")

    def __str__(self):
        return f"{self.lot} {self.city} {self.state}"


class Contact(BaseModel):
    TYPE = (
        ('Contact', 'Contact'),
        ('Client', 'Client'),
        ('Info', 'Info'),
        ('Personal', 'Personal'),
    )
    value = models.CharField(max_length=15)
    type = models.CharField(default='Client', max_length=50, choices=TYPE)

    def __str__(self):
        return self.value


class Degree(BaseModel):
    name = models.CharField(max_length=150)
    stars = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ],
        choices=[(i, str(i)) for i in range(6)], null=True, blank=True
    )

    def __str__(self):
        return self.name


class Email(BaseModel):
    TYPE = (
        ('Contact', 'Contact'),
        ('Client', 'Client'),
        ('Info', 'Info'),
        ('Personal', 'Personal'),
    )
    value = models.CharField(max_length=250)
    type = models.CharField(default='Client', max_length=50, choices=TYPE)

    def __str__(self):
        return f"{self.type} : {self.value}"


class Web(BaseModel):
    TYPE = (
        ('Blog', 'Blog'),
        ('CV', 'CV'),
        ('Portfolio', 'Portfolio'),
        ('Works', 'Works'),
    )
    title = models.CharField(max_length=150)
    url = models.URLField()
    type = models.CharField(default='Works', max_length=50, choices=TYPE)

    def __str__(self):
        return self.title


class Social(BaseModel):
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=25, choices=SOCIALS)
    url = models.URLField()

    def __str__(self):
        return self.title


class About(ImageModel):
    title = models.CharField(max_length=150)
    introduction = models.TextField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class Profile(BaseModel, ImageModel):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    pseudo = models.CharField(max_length=50)
    birthday = models.DateField()
    degrees = models.ManyToManyField(Degree, blank=True)
    contacts = models.ManyToManyField(Contact, blank=True)
    emails = models.ManyToManyField(Email, blank=True)
    socials = models.ManyToManyField(Social, blank=True)
    webs = models.ManyToManyField(Web, blank=True)
    localisation = models.ForeignKey(Localisation, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
