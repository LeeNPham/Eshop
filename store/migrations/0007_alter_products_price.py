# Generated by Django 4.1 on 2022-08-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_order_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
