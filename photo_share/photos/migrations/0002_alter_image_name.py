# Generated by Django 4.2.3 on 2023-07-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
