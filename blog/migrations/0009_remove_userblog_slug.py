# Generated by Django 3.0 on 2020-12-08 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_userblog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userblog',
            name='slug',
        ),
    ]
