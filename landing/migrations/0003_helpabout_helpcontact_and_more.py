# Generated by Django 5.0.1 on 2024-01-29 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_questionbox_frequentlyaskedquestions'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('title1', models.CharField(blank=True, max_length=50, null=True)),
                ('description1', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HelpContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='frequentlyaskedquestions',
            name='question_box',
        ),
        migrations.RenameField(
            model_name='frequentlyaskedquestions',
            old_name='description',
            new_name='answer',
        ),
        migrations.RemoveField(
            model_name='frequentlyaskedquestions',
            name='title',
        ),
        migrations.AddField(
            model_name='frequentlyaskedquestions',
            name='question',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='landingsubscription',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='QuestionBox',
        ),
    ]