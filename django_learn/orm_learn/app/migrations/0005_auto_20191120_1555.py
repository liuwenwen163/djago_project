# Generated by Django 2.1.2 on 2019-11-20 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(blank=True, db_index=True, default=0),
        ),
    ]
