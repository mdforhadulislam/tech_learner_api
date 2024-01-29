# Generated by Django 5.0.1 on 2024-01-29 10:05

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_accessbook_access_book_and_more'),
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreadedchartdata',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 1, 29, 16, 5, 50, 902586), null=True),
        ),
        migrations.AlterField(
            model_name='sitevisitedchartdata',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 1, 29, 16, 5, 50, 902586), null=True),
        ),
        migrations.CreateModel(
            name='ReadedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readed_book', models.ManyToManyField(blank=True, to='books.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
