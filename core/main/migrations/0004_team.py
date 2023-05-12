# Generated by Django 4.2.1 on 2023-05-12 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_aboutpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='Image')),
                ('social1', models.CharField(max_length=50, verbose_name='Social 1')),
                ('social2', models.CharField(max_length=50, verbose_name='Social 2')),
                ('social3', models.CharField(max_length=50, verbose_name='Social 3')),
                ('social4', models.CharField(max_length=50, verbose_name='Social 4')),
                ('social_url1', models.URLField(verbose_name='Social Url 1')),
                ('social_url2', models.URLField(verbose_name='Social Url 2')),
                ('social_url3', models.URLField(verbose_name='Social Url 3')),
                ('social_url4', models.URLField(verbose_name='Social Url 4')),
                ('title', models.CharField(max_length=50, verbose_name='Name')),
                ('subtitle', models.CharField(max_length=50, verbose_name='Profession')),
                ('text', models.TextField(verbose_name='Info')),
            ],
        ),
    ]
