# Generated by Django 4.1.3 on 2022-12-08 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proKApp', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prodcut_image',
            new_name='product_image',
        ),
    ]