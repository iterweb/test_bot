from django.db import models
from preferences.models import Preferences


class Profile(models.Model):
    tg_id = models.PositiveIntegerField(unique=True, verbose_name='Telegram ID')
    first_start = models.DateTimeField(auto_now_add=True, verbose_name='First Start')
    tg_username = models.CharField(max_length=250, verbose_name='User Name', blank=True, null=True)
    tg_firstname = models.CharField(max_length=250, verbose_name='First Name', blank=True, null=True)
    tg_lastname = models.CharField(max_length=250, verbose_name='Last Name', blank=True, null=True)

    def __str__(self):
        return f'{self.tg_id} - {self.tg_username}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class BotPreferences(Preferences):
    btc = models.CharField(max_length=25, verbose_name='btc', default='BTC')
    eth = models.CharField(max_length=25, verbose_name='eth', default='ETH')
    doge = models.CharField(max_length=25, verbose_name='doge', default='DOGE')
    error_message = models.TextField(default='Error')
    welcome = models.TextField(default='Hello!')

    class Meta:
        verbose_name = 'Bot Setting'
        verbose_name_plural = 'Bot Settings'
