# Generated by Django 4.1.5 on 2023-02-15 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_otp_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(days=-1, seconds=68400)),
        ),
    ]
