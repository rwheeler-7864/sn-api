# Generated by Django 3.1.2 on 2020-10-30 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_recordlocator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenttransaction',
            name='transaction_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
