# Generated by Django 2.2.12 on 2021-12-24 23:15

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0002_auto_20211224_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='platform',
        ),
        migrations.AddField(
            model_name='player',
            name='first',
            field=otree.db.models.FloatField(null=True, verbose_name='Your Preferences'),
        ),
        migrations.AddField(
            model_name='player',
            name='second',
            field=otree.db.models.FloatField(null=True, verbose_name='Your Preferences'),
        ),
        migrations.AddField(
            model_name='player',
            name='third',
            field=otree.db.models.FloatField(null=True, verbose_name='Your Preferences'),
        ),
    ]