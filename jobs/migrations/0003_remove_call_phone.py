# Generated by Django 3.1.2 on 2021-06-24 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210622_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='call',
            name='phone',
        ),
    ]