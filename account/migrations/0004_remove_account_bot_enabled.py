# Generated by Django 2.1.5 on 2019-02-18 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190218_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='bot_enabled',
        ),
    ]
