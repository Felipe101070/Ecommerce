# Generated by Django 4.0.3 on 2022-05-07 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_bought',
            field=models.IntegerField(default=0),
        ),
    ]
