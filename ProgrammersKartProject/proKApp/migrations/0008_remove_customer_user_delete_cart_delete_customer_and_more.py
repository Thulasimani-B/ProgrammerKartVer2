# Generated by Django 4.1.3 on 2022-12-20 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proKApp', '0007_remove_product_prodapp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
