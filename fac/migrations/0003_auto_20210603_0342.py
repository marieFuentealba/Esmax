# Generated by Django 2.2 on 2021-06-03 07:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0005_auto_20210427_0128'),
        ('fac', '0002_facturadet_facturaenc'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FacturaDet',
            new_name='FacturaDeta',
        ),
    ]
