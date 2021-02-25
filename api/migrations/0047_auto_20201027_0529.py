# Generated by Django 3.1.2 on 2020-10-27 05:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_auto_20201027_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttransaction',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.booking'),
        ),
        migrations.AlterField(
            model_name='providerchain',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterModelTable(
            name='paymenttransaction',
            table='payment_transaction',
        ),
    ]