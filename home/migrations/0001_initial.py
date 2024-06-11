# Generated by Django 5.0.6 on 2024-06-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.TextField()),
                ('avaliable_rooms', models.IntegerField()),
            ],
        ),
    ]
