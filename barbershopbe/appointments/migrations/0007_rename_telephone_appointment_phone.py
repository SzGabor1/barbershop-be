# Generated by Django 5.0.1 on 2024-04-22 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_appointment_telephone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='telephone',
            new_name='phone',
        ),
    ]
