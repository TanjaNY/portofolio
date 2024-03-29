# Generated by Django 3.1.2 on 2021-07-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_remove_call_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=300)),
                ('url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
