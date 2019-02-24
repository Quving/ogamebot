# Generated by Django 2.1.5 on 2019-02-24 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fleet', to='planet.Planet')),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=24)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Battlecruiser',
            fields=[
                ('ship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fleet.Ship')),
            ],
            bases=('fleet.ship',),
        ),
        migrations.CreateModel(
            name='Battleship',
            fields=[
                ('ship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fleet.Ship')),
            ],
            bases=('fleet.ship',),
        ),
        migrations.CreateModel(
            name='Bomber',
            fields=[
                ('ship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fleet.Ship')),
            ],
            bases=('fleet.ship',),
        ),
        migrations.CreateModel(
            name='ColonyShip',
            fields=[
                ('ship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fleet.Ship')),
            ],
            bases=('fleet.ship',),
        ),
        migrations.CreateModel(
            name='Cruiser',
            fields=[
                ('ship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fleet.Ship')),
            ],
            bases=('fleet.ship',),
        ),
        migrations.CreateModel(
            name='Deathstar',
            fields=[
                ('ship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fleet.Ship')),
            ],
            bases=('fleet.ship',),
        ),
        migrations.CreateModel(
            name='Destroyer',
            fields=[
                ('ship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fleet.Ship')),
            ],
            bases=('fleet.ship',),
        ),
        migrations.CreateModel(
            name='HeavyFiter',
            fields=[
                ('ship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fleet.Ship')),
            ],
            bases=('fleet.ship',),
        ),
        migrations.CreateModel(
            name='LargeCargo',
            fields=[
                ('ship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fleet.Ship')),
            ],
            bases=('fleet.ship',),
        ),
        migrations.CreateModel(
            name='LittleFiter',
            fields=[
                ('ship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fleet.Ship')),
            ],
            bases=('fleet.ship',),
        ),
        migrations.CreateModel(
            name='Recycler',
            fields=[
                ('ship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fleet.Ship')),
            ],
            bases=('fleet.ship',),
        ),
        migrations.CreateModel(
            name='SmallCargo',
            fields=[
                ('ship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fleet.Ship')),
            ],
            bases=('fleet.ship',),
        ),
    ]
