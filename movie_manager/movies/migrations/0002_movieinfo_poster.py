# Generated by Django 5.2.1 on 2025-06-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='poster',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
