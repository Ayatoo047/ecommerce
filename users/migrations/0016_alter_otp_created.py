# Generated by Django 4.1.5 on 2023-02-16 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_otp_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
