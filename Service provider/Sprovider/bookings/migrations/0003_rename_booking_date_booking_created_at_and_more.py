# Generated by Django 5.1.5 on 2025-02-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_booking_payment_mode_booking_payment_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='booking',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='customer_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='customer_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
