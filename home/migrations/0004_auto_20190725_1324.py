# Generated by Django 2.1.7 on 2019-07-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190725_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='product',
            field=models.ManyToManyField(blank=True, to='home.Product'),
        ),
    ]