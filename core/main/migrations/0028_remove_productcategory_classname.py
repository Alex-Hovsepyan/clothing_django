# Generated by Django 4.2.1 on 2023-05-13 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_product_options_productcategory_classname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='classname',
        ),
    ]
