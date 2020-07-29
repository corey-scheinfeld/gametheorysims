# Generated by Django 2.2.12 on 2020-07-29 13:54

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('total_participants', otree.db.models.IntegerField(null=True)),
                ('bonus', otree.db.models.IntegerField(null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participation_group', to='otree.Session')),
            ],
            options={
                'db_table': 'participation_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('winner', otree.db.models.StringField(max_length=10000, null=True)),
                ('alpha', otree.db.models.IntegerField(null=True)),
                ('beta', otree.db.models.IntegerField(null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participation_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'participation_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('group_type', otree.db.models.StringField(max_length=10000, null=True)),
                ('group_bonus', otree.db.models.IntegerField(null=True)),
                ('personal_bonus', otree.db.models.IntegerField(null=True)),
                ('choice', otree.db.models.StringField(choices=[('Participate', 'Participate'), ('Do Not Participate', 'Do Not Participate')], max_length=10000, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='participation.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participation_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participation_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participation.Subsession')),
            ],
            options={
                'db_table': 'participation_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participation.Subsession'),
        ),
    ]
