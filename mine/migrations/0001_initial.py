# Generated by Django 2.1.7 on 2019-03-21 16:37

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
                ('level', models.IntegerField(default=0)),
                ('upgradeable', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=24)),
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
            name='FusionReactor',
            fields=[
                ('mine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mine.Mine')),
            ],
            bases=('mine.mine',),
        ),
        migrations.CreateModel(
            name='MetalMine',
            fields=[
                ('mine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mine.Mine')),
            ],
            bases=('mine.mine',),
        ),
        migrations.CreateModel(
            name='SolarPowerstation',
            fields=[
                ('mine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mine.Mine')),
            ],
            bases=('mine.mine',),
        ),
        migrations.CreateModel(
            name='SolarSatellite',
            fields=[
                ('mine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mine.Mine')),
            ],
            bases=('mine.mine',),
        ),
        migrations.AddField(
            model_name='mine',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mines', to='planet.Planet'),
        ),
    ]
