# Generated by Django 2.1.5 on 2019-02-27 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0003_auto_20190224_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='id',
            field=models.IntegerField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]