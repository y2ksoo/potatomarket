# Generated by Django 2.2.14 on 2020-09-14 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wares', '0006_auto_20200812_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ware',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
