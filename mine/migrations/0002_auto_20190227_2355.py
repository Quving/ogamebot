# Generated by Django 2.1.5 on 2019-02-27 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mine',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='mine',
            name='uptimed_at',
        ),
    ]
