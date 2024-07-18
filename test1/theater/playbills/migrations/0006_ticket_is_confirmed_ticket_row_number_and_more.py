# Generated by Django 5.0.4 on 2024-05-21 03:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("playbills", "0005_playbill_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="is_confirmed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="ticket",
            name="row_number",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="ticket",
            name="seat_number",
            field=models.CharField(max_length=10, null=True),
        ),
    ]