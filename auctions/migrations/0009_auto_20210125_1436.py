# Generated by Django 3.1.5 on 2021-01-25 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210125_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activelistings',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.categories'),
        ),
    ]
