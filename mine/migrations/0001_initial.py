# Generated by Django 2.1.5 on 2019-02-18 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('level', models.IntegerField(default=0)),
                ('upgradeable', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CrystalMine',
            fields=[
                ('mine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mine.Mine')),
            ],
            bases=('mine.mine',),
        ),
        migrations.CreateModel(
            name='DeuteriumMine',
            fields=[
                ('mine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mine.Mine')),
            ],
            bases=('mine.mine',),
        ),
        migrations.CreateModel(
            name='IronMine',
            fields=[
                ('mine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mine.Mine')),
            ],
            bases=('mine.mine',),
        ),
        migrations.AddField(
            model_name='mine',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planet.Planet'),
        ),
    ]
