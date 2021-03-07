# Generated by Django 3.1.5 on 2021-01-25 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20210125_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activelistings',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='auctions.categories'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='Category',
            field=models.CharField(max_length=25),
        ),
    ]