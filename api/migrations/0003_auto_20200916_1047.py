# Generated by Django 3.0.6 on 2020-09-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier_priceline',
            name='cityid_ppn1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier_priceline',
            name='hotelid_ppn1',
            field=models.TextField(blank=True, null=True),
        ),
    ]