# Generated by Django 3.0 on 2020-12-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_userblog_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tit', models.CharField(max_length=10)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]