# Generated by Django 3.1.2 on 2021-01-22 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0075_auto_20210122_1834"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venuecontact",
            name="venue_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="contacts", to="api.venue"
            ),
        ),
        migrations.AlterField(
            model_name="venuedetail",
            name="venue_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="details", to="api.venue"
            ),
        ),
    ]
