# Generated by Django 2.2.3 on 2019-07-25 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190725_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quantity',
            old_name='products',
            new_name='product',
        ),
    ]
