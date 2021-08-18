from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

from .models import Profile, BotPreferences


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'tg_id', 'tg_username', 'tg_firstname', 'tg_lastname', 'first_start']


@admin.register(BotPreferences)
class PreferencesAdmin(admin.ModelAdmin):
    list_display = ['btc', 'eth', 'doge', 'error_message', 'welcome']
    list_display_links = ['btc', 'eth', 'doge']
    exclude = ['sites']


admin.site.unregister(Site)
admin.site.unregister(Group)