# Generated by Django 2.2 on 2021-05-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vnt', '0002_ventasdet_ventasenc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventasenc',
            name='fecha_factura',
            field=models.DateField(blank=True, null=True),
        ),
    ]
