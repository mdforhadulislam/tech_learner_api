# Generated by Django 5.0.1 on 2024-01-29 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_bookreadedchartdata_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreadedchartdata',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 1, 29, 21, 21, 28, 112677), null=True),
        ),
        migrations.AlterField(
            model_name='sitevisitedchartdata',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 1, 29, 21, 21, 28, 113676), null=True),
        ),
    ]
