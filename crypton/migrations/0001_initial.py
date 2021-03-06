# Generated by Django 3.2.6 on 2021-08-18 08:51

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('preferences', '0003_alter_preferences_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotPreferences',
            fields=[
                ('preferences_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='preferences.preferences')),
                ('btc', models.CharField(default='BTC', max_length=25, verbose_name='btc')),
                ('eth', models.CharField(default='ETH', max_length=25, verbose_name='eth')),
                ('doge', models.CharField(default='DOGE', max_length=25, verbose_name='doge')),
                ('error_message', models.TextField(default='Error')),
                ('welcome', models.TextField(default='Hello!')),
            ],
            options={
                'verbose_name': 'Bot Setting',
                'verbose_name_plural': 'Bot Settings',
            },
            bases=('preferences.preferences',),
            managers=[
                ('singleton', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.PositiveIntegerField(unique=True, verbose_name='Telegram ID')),
                ('first_start', models.DateTimeField(auto_now_add=True, verbose_name='First Start')),
                ('tg_username', models.CharField(blank=True, max_length=250, null=True, verbose_name='User Name')),
                ('tg_firstname', models.CharField(blank=True, max_length=250, null=True, verbose_name='First Name')),
                ('tg_lastname', models.CharField(blank=True, max_length=250, null=True, verbose_name='Last Name')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
