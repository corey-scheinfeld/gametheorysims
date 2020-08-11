# Generated by Django 2.2.12 on 2020-08-11 13:09

from django.db import migrations, models
import django.db.models.deletion
import otree.currency
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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricecomp_group', to='otree.Session')),
            ],
            options={
                'db_table': 'priceComp_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pricecomp_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'priceComp_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('choice', otree.db.models.IntegerField(choices=[[1, otree.currency.Currency('1.00')], [2, otree.currency.Currency('2.00')], [3, otree.currency.Currency('3.00')]], null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='priceComp.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricecomp_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricecomp_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='priceComp.Subsession')),
            ],
            options={
                'db_table': 'priceComp_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='priceComp.Subsession'),
        ),
    ]