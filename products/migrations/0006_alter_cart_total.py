# Generated by Django 4.1.4 on 2022-12-31 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_cart_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
