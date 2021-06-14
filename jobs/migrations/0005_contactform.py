# Generated by Django 3.1.2 on 2021-06-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20200827_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=400)),
                ('phone', models.CharField(max_length=400)),
                ('message', models.TextField(max_length=2000)),
            ],
        ),
    ]
