# Generated by Django 3.1.2 on 2020-12-07 05:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0060_auto_20201122_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_code', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('review_count', models.IntegerField()),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.provider')),
            ],
            options={
                'db_table': 'provider_review',
            },
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.CreateModel(
            name='ProviderReviewContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('review_text', models.TextField(null=True)),
                ('good_text', models.TextField(null=True)),
                ('bad_text', models.TextField(null=True)),
                ('overall_description', models.TextField(null=True)),
                ('provider_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.providerreview')),
            ],
            options={
                'db_table': 'provider_review_content',
            },
        ),
        migrations.AddIndex(
            model_name='providerreview',
            index=models.Index(fields=['provider', 'provider_code'], name='provider_re_provide_365d38_idx'),
        ),
    ]