# Generated by Django 2.1.5 on 2019-02-21 02:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0003_auto_20190221_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='mine',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mine',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
