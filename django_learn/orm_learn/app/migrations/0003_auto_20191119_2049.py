# Generated by Django 2.1.2 on 2019-11-19 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_test_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='age',
            new_name='ages',
        ),
    ]