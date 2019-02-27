# Generated by Django 2.1.7 on 2019-02-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logEntry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]