# Generated by Django 2.2.12 on 2022-01-05 22:09

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prisoner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='partner_decision',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
