# Generated by Django 4.2.11 on 2024-03-14 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("weather_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="weatherdata",
            old_name="ann",
            new_name="autumn_mean",
        ),
        migrations.RenameField(
            model_name="weatherdata",
            old_name="aut",
            new_name="spring_mean",
        ),
        migrations.RenameField(
            model_name="weatherdata",
            old_name="spr",
            new_name="summer_mean",
        ),
        migrations.RenameField(
            model_name="weatherdata",
            old_name="sum",
            new_name="winter_mean",
        ),
        migrations.RemoveField(
            model_name="weatherdata",
            name="win",
        ),
        migrations.AddField(
            model_name="weatherdata",
            name="annual_mean",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="weatherdata",
            name="last_updated",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="apr",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="aug",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="dec",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="feb",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="jan",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="jul",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="jun",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="mar",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="may",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="nov",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="oct",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="sep",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="year",
            field=models.IntegerField(unique=True),
        ),
    ]
