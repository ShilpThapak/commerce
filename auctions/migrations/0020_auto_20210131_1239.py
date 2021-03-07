# Generated by Django 3.1.5 on 2021-01-31 07:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auto_20210131_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='savedlistings',
        ),
        migrations.AddField(
            model_name='activelistings',
            name='userswhosaved',
            field=models.ManyToManyField(blank=True, related_name='savedlistings', to=settings.AUTH_USER_MODEL),
        ),
    ]
