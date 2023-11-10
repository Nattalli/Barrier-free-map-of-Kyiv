# Generated by Django 4.1 on 2023-11-10 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pointer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mappoint",
            name="schedule",
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name="mappoint",
            name="address",
            field=models.CharField(default="Unknown", max_length=255),
        ),
        migrations.AlterField(
            model_name="mappoint",
            name="latitude",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="mappoint",
            name="longitude",
            field=models.FloatField(default=0.0),
        ),
    ]