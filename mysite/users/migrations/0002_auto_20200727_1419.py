# Generated by Django 2.2.14 on 2020-07-27 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='trustseller',
            field=models.BooleanField(default=False, verbose_name='trust seller'),
        ),
    ]
