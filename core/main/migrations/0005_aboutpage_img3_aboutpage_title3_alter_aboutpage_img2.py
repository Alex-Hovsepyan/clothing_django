# Generated by Django 4.2.1 on 2023-05-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='img3',
            field=models.ImageField(default=11, upload_to='images', verbose_name='Image 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='title3',
            field=models.CharField(default=1, max_length=50, verbose_name='Title 3'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='img2',
            field=models.ImageField(upload_to='images', verbose_name='Image 1'),
        ),
    ]