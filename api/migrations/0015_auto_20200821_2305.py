# Generated by Django 3.0.6 on 2020-08-21 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200821_0516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crscity',
            old_name='province_code',
            new_name='province',
        ),
        migrations.AlterField(
            model_name='crscity',
            name='provider_code',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
