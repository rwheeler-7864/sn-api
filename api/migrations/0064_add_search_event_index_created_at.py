# Generated by Django 3.1.2 on 2020-12-16 07:22

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("api", "0063_add_search_event_index_request_id"),
    ]

    operations = [migrations.RunSQL("CREATE INDEX CONCURRENTLY ON search_events(created_at)")]