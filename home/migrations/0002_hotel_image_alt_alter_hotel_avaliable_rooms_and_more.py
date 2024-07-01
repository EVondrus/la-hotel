# Generated by Django 5.0.6 on 2024-06-30 16:44

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='image_alt',
            field=models.CharField(default='placeholder default hotel image', help_text='Enter a breif description of the image', max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='avaliable_rooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(help_text='Enter a description of the hotel'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[550, None], upload_to='hotel'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]