# Generated by Django 5.0.1 on 2024-04-22 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_alter_appointment_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='staff',
        ),
    ]
