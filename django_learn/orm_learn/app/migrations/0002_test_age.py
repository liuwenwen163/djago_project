# Generated by Django 2.1.2 on 2019-11-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='age',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]