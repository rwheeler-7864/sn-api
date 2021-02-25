# Generated by Django 3.0.6 on 2020-09-29 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_providerimages'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='providerimages',
            index=models.Index(fields=['provider', 'provider_code'], name='provider_im_provide_a42793_idx'),
        ),
    ]