# Generated by Django 2.2.14 on 2020-07-27 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basicmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wares.BasicModel')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Room Type',
                'ordering': ['created'],
            },
            bases=('wares.basicmodel',),
        ),
        migrations.CreateModel(
            name='Ware',
            fields=[
                ('basicmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wares.BasicModel')),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('city', models.CharField(max_length=80)),
                ('category', models.ManyToManyField(blank=True, related_name='ware', to='wares.Category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ware', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('wares.basicmodel',),
        ),
    ]
