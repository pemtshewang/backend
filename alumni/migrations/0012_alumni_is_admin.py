# Generated by Django 4.1 on 2022-10-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("alumni", "0011_alter_alumni_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="alumni",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
