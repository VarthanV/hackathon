# Generated by Django 2.2.3 on 2019-07-25 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190725_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='home.Product'),
        ),
    ]
