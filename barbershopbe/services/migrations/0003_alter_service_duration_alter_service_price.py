# Generated by Django 5.0.1 on 2024-04-08 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_user_alter_service_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
