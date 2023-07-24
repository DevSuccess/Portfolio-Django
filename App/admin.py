from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


# Register your models here.
@admin.register(models.Localisation)
class LocalisationAdmin(admin.ModelAdmin):
    list_display = ('lot', 'street', 'city', 'state', 'zip_code', 'admin_map')
    fields = ('lot', 'street', 'city', 'state', 'zip_code', 'map', 'admin_map')
    readonly_fields = ('admin_map',)

    def admin_map(self, obj):
        return mark_safe(obj.map)

    admin_map.short_description = 'Map'


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('value', 'type', 'active', 'created_at', 'updated_at')
    fields = ('value', 'type', 'active', ('created_at', 'updated_at'))
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars', 'active', 'created_at', 'updated_at')
    fields = ['name', 'stars', 'active', ('created_at', 'updated_at')]
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('value', 'type', 'active', 'created_at', 'updated_at')
    fields = ('value', 'type', 'active', ('created_at', 'updated_at'))
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.Web)
class WebAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'type', 'active', 'created_at', 'updated_at')
    fields = ('title', 'url', 'type', 'active', ('created_at', 'updated_at'))
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'type', 'active', 'created_at', 'updated_at')
    fields = ('title', 'url', 'type', 'active', ('created_at', 'updated_at'))
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'introduction', 'admin_photo')
    fields = ('title', 'introduction', 'description', 'admin_photo')
    readonly_fields = ('admin_photo',)


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'pseudo', 'birthday',)
    filter_horizontal = ('degrees', 'contacts', 'emails', 'socials', 'webs')
    fieldsets = (
        ('Personal', {
            'fields': ('firstname', 'lastname', 'pseudo', 'birthday',)
        }),
        (None, {
            'fields': ('image', 'degrees')
        }),
        ('Contacts and Emails', {
            'fields': ('contacts', 'emails')
        }),
        ('Socials and Web', {
            'fields': ('socials', 'webs')
        }),
    )
    readonly_fields = ('admin_photo', 'created_at', 'updated_at')


