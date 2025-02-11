# Generated by Django 5.1.5 on 2025-02-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customerprofile_name_providerprofile_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True),
        ),
    ]
