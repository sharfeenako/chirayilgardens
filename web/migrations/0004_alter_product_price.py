# Generated by Django 4.0.6 on 2023-08-28 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
