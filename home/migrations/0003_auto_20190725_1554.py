# Generated by Django 2.2.3 on 2019-07-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190725_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imgs',
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
