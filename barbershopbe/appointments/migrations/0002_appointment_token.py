# Generated by Django 5.0.1 on 2024-04-11 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='token',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
