# Generated by Django 4.1.7 on 2023-03-06 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("LittleLemonAPI", "0008_remove_menuitem_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="menuitem",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="LittleLemonAPI.category",
            ),
        ),
    ]
