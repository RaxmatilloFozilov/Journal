# Generated by Django 5.0.6 on 2024-05-22 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirements',
            name='connection',
        ),
    ]