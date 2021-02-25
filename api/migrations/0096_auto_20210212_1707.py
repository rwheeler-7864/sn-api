# Generated by Django 3.1.2 on 2021-02-12 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0095_auto_20210212_1705"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productshotelroomdetails",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="hotels_room_details",
                to="api.producthotel",
            ),
        ),
        migrations.AlterField(
            model_name="productshotelroompricing",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="hotels_room_pricing",
                to="api.producthotel",
            ),
        ),
    ]
