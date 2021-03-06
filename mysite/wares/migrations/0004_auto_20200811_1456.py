# Generated by Django 2.2.14 on 2020-08-11 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wares', '0003_ware_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ware',
            name='photo',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('basicmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wares.BasicModel')),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='ware_photos')),
                ('wares', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='wares.Ware')),
            ],
            bases=('wares.basicmodel',),
        ),
    ]
