# Generated by Django 2.2.7 on 2021-01-25 07:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qpoll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 25, 7, 10, 43, 106020, tzinfo=utc)),
        ),
    ]
