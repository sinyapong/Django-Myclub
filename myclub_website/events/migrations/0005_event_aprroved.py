# Generated by Django 4.2.5 on 2023-12-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_venue_venue_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='aprroved',
            field=models.BooleanField(default=False, verbose_name='Aprroved'),
        ),
    ]
