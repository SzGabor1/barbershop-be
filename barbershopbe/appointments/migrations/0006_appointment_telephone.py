# Generated by Django 5.0.1 on 2024-04-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_remove_appointment_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='telephone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
