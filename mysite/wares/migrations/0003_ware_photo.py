# Generated by Django 2.2.14 on 2020-08-11 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wares', '0002_auto_20200729_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='ware',
            name='photo',
            field=models.ImageField(blank=True, upload_to='ware_photos'),
        ),
    ]