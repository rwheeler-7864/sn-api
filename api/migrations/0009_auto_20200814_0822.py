# Generated by Django 3.0.6 on 2020-08-14 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200813_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrsCity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('provider_code', models.TextField()),
                ('location_name', models.TextField()),
                ('province_code', models.TextField()),
                ('country_code', models.CharField(max_length=2)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=11)),
            ],
            options={
                'db_table': 'crs_cities',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'providers',
            },
        ),

        migrations.AddField(
            model_name='crscity',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Provider'),
        ),
    ]
