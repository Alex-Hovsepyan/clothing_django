# Generated by Django 4.2.1 on 2023-05-13 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_hometitle_class1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hometitle',
            name='class1',
        ),
    ]