# Generated by Django 4.2.3 on 2023-07-29 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("image", models.ImageField(upload_to="images/")),
                (
                    "status",
                    models.CharField(
                        choices=[("public", "Public"), ("private", "Private")],
                        default="public",
                        max_length=7,
                    ),
                ),
                ("upload_date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-upload_date"],
                "indexes": [
                    models.Index(fields=["name"], name="name_idx"),
                    models.Index(fields=["user"], name="user_idx"),
                ],
            },
        ),
    ]
