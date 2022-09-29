from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Käyttäjä, Organisaatio

class KäyttäjäInline(admin.TabularInline):
    model = Käyttäjä
    extra = 0

@admin.register(Organisaatio)
class OrganisaatioAdmin(admin.ModelAdmin):
    inlines = [KäyttäjäInline]

@admin.register(Käyttäjä)
class KäyttäjäAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'organization')
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email', ('first_name', 'last_name', 'organization'))
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions')
        })
    )