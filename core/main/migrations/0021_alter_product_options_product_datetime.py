# Generated by Django 4.2.1 on 2023-05-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_homeproducttitle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['datetime']},
        ),
        migrations.AddField(
            model_name='product',
            name='datetime',
            field=models.DateField(auto_now=True, verbose_name='Datetime'),
        ),
    ]