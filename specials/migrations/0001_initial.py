# Generated by Django 5.0.6 on 2024-10-20 23:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Special",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("limitations", models.TextField(blank=True)),
                (
                    "day_of_week",
                    models.CharField(
                        choices=[
                            ("Monday", "Monday"),
                            ("Tuesday", "Tuesday"),
                            ("Wednesday", "Wednesday"),
                            ("Thursday", "Thursday"),
                            ("Friday", "Friday"),
                            ("Saturday", "Saturday"),
                            ("Sunday", "Sunday"),
                        ],
                        max_length=9,
                    ),
                ),
                ("start_time", models.TimeField(null=True)),
                ("end_time", models.TimeField(null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("location", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="locations.location")),
            ],
        ),
    ]
