# Generated by Django 5.1.5 on 2025-02-08 19:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='average_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='service',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
