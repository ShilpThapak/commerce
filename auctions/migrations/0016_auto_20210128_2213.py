# Generated by Django 3.1.5 on 2021-01-28 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_bid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bid',
            new_name='bids',
        ),
    ]
