# Generated by Django 3.0.6 on 2020-08-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200818_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='hote_listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.TextField(blank=True, null=True)),
                ('hotelid', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('hotelname', models.TextField(blank=True, null=True)),
                ('zipcode', models.TextField(blank=True, null=True)),
                ('stars', models.FloatField(blank=True, null=True)),
                ('countrycode', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('simplenight_id', models.IntegerField()),
            ],
        ),
    ]