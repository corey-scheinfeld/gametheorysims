# Generated by Django 2.2.12 on 2022-01-05 22:16

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('trust', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='role',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]