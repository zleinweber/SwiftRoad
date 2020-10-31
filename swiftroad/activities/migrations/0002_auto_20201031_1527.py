# Generated by Django 3.1.2 on 2020-10-31 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="activity",
            options={"verbose_name_plural": "activities"},
        ),
        migrations.AlterField(
            model_name="activity",
            name="distance",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="activity",
            name="duration",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="activity",
            name="steps",
            field=models.IntegerField(default=0),
        ),
    ]
