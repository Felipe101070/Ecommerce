# Generated by Django 4.0.3 on 2022-04-08 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_active_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug_padrao'),
            preserve_default=False,
        ),
    ]