# Generated by Django 2.2 on 2021-06-11 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0005_auto_20210427_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='existencia',
            field=models.IntegerField(default=12),
        ),
    ]
