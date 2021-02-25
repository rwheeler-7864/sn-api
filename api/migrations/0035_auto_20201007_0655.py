# Generated by Django 3.0.6 on 2020-10-07 06:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_auto_20201007_0553'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderHotel',
            fields=[
                ('provider_hotel_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('provider_code', models.TextField()),
                ('language_code', models.CharField(default='en', max_length=2)),
                ('hotel_name', models.TextField()),
                ('city_name', models.TextField(null=True)),
                ('state', models.TextField(null=True)),
                ('country_code', models.CharField(max_length=2, null=True)),
                ('address_line_1', models.TextField(null=True)),
                ('address_line_2', models.TextField(null=True)),
                ('postal_code', models.CharField(max_length=10, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Provider')),
            ],
            options={
                'db_table': 'provider_hotel',
            },
        ),
        migrations.AddIndex(
            model_name='providerhotel',
            index=models.Index(fields=['provider', 'provider_code'], name='provider_ho_provide_c6e210_idx'),
        ),
    ]
