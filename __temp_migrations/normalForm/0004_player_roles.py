# Generated by Django 2.2.12 on 2022-01-06 00:51

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('normalForm', '0003_auto_20220105_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='roles',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
