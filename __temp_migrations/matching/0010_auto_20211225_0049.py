# Generated by Django 2.2.12 on 2021-12-25 05:49

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0009_auto_20211224_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='round',
        ),
        migrations.AddField(
            model_name='player',
            name='round',
            field=otree.db.models.IntegerField(default=1, null=True),
        ),
    ]