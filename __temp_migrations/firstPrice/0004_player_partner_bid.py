# Generated by Django 2.2.12 on 2022-01-05 21:25

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPrice', '0003_player_partner_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='partner_bid',
            field=otree.db.models.FloatField(null=True),
        ),
    ]
