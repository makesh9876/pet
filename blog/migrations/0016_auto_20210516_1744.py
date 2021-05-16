# Generated by Django 3.0 on 2021-05-16 12:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210516_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='req',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='req',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]