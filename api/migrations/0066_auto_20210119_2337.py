# Generated by Django 3.1.2 on 2021-01-19 23:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0065_auto_20210119_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, choices=[('VIDEO', 'VIDEO'), ('IMAGE', 'IMAGE')], max_length=8, null=True)),
                ('image_url', models.TextField()),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.venue')),
            ],
            options={
                'verbose_name': 'Venue Image',
                'verbose_name_plural': 'Venue Images',
                'db_table': 'api_venue_images',
            },
        ),
    ]
