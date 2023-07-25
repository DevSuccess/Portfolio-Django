from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


# Register your models here.
@admin.register(models.Icon)
class IconAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_or_id', 'icon_style')
    fields = ('name', 'class_or_id', 'icon_style')


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
    list_display = ('value', 'icons', 'active', 'privilege', 'created_at', 'updated_at')
    fields = ('value', 'icons', ('active', 'privilege'), ('created_at', 'updated_at'))
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars', 'active', 'created_at', 'updated_at')
    fields = ['name', 'stars', 'active', ('created_at', 'updated_at')]
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('value', 'icons', 'active', 'created_at', 'updated_at')
    fields = ('value', 'icons', 'active', ('created_at', 'updated_at'))
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.Web)
class WebAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'icons', 'active', 'privilege', 'created_at', 'updated_at')
    fields = ('title', 'url', 'icons', ('active', 'privilege'), ('created_at', 'updated_at'))
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'icons', 'active', 'created_at', 'updated_at')
    fields = ('title', 'url', 'icons', 'active', ('created_at', 'updated_at'))
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ('title', 'introduction')
    fields = ('title', 'introduction', 'description')


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'pseudo', 'birthday', 'admin_photo')
    filter_horizontal = ('degrees', 'socials')
    fieldsets = (
        ('Personal', {
            'fields': ('firstname', 'lastname', 'pseudo', 'birthday', 'localisation')
        }),
        (None, {
            'fields': ('image', 'degrees')
        }),
        ('Contacts and Emails', {
            'fields': ('contact', 'email')
        }),
        ('Socials and Web', {
            'fields': ('socials', 'web')
        })
    )
    readonly_fields = ('admin_photo', 'created_at', 'updated_at')


@admin.register(models.Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ('count', 'phrase_begin', 'phrase_end', 'icons')
    fields = ('count', 'phrase_begin', 'phrase_end', 'icons')


@admin.register(models.Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'admin_photo')
    fields = ('name', 'rate', 'image', 'admin_photo')
    readonly_fields = ('admin_photo',)


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('libel', 'created_at', 'updated_at')
    filter_horizontal = ('competences',)
    fieldsets = (
        (None, {
            'fields': ('libel', 'active')
        }),
        ('Competences', {
            'fields': ('competences', 'created_at', 'updated_at')
        })
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('value',)
    fields = ('value',)


@admin.register(models.Summary)
class TitleResumeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'details', 'lists')
    filter_horizontal = ('lists',)


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'begin', 'end',)
    fields = ('title', 'begin', 'end', 'description', 'details')


@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'begin', 'end', 'description')
    fields = ('title', 'begin', 'end', 'description', 'lists')
    filter_horizontal = ('lists',)


@admin.register(models.SectionType)
class SectionTypeAdmin(admin.ModelAdmin):
    list_display = ('value', 'active', 'icons')
    fields = ('value', 'active', 'icons')


@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'active', 'created_at', 'updated_at')
    fields = ('title', 'type', 'active', ('created_at', 'updated_at'))
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.ImagePortfolio)
class ImagePortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_photo')
    fields = ('name', 'admin_photo', 'image')
    readonly_fields = ('admin_photo',)


@admin.register(models.CategoryPortfolio)
class CategoryPortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    fields = ('name', 'value')


@admin.register(models.ClientPortfolio)
class ClientPortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact')
    fields = ('name', 'contact')


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'begin', 'end')
    fieldsets = (
        (None, {
            'fields': ('name', 'url', 'begin', 'end', 'active')
        }),
        ('Details', {
            'fields': ('details', 'category', 'client')
        }),
        ('Images', {
            "fields": ('images', )
        })
    )
    filter_horizontal = ('images',)
