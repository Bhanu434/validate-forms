# Generated by Django 4.2.6 on 2024-01-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='Semali',
            field=models.EmailField(default='school@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='school',
            name='SreenterEmail',
            field=models.EmailField(default='school@gmail.com', max_length=254),
        ),
    ]
