# Generated by Django 3.1.5 on 2021-01-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='activelistings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=64)),
                ('startingbid', models.IntegerField()),
                ('imageurl', models.BinaryField()),
                ('category', models.CharField(max_length=64)),
            ],
        ),
    ]