# Generated by Django 3.1.2 on 2021-06-22 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='call',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='call',
            name='message',
            field=models.TextField(max_length=300),
        ),
    ]
