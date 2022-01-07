from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
import random

"""
Sim for 'Matching Pennies' game
"""


class Constants(BaseConstants):
    name_in_url = 'pennies'
    players_per_group = 2
    num_rounds = 12

    instructions_template = 'pennies/instructions.html'
    row_role = 'Row'
    col_role = 'Column'


class Subsession(BaseSubsession):
    stage = models.IntegerField()
    def creating_session(self):
        self.stage  = 1
        if self.round_number == 1:
            self.group_randomly()
            for p in self.get_players():
                p.participant.vars['total'] = 0
        else:
            if self.round_number >= 5 and self.round_number <9:
                self.group_randomly()
                self.stage  = 2
            elif self.round_number >= 9:
                self.group_randomly()
                self.stage  = 3
            else:
                self.group_like_round(self.round_number - 1)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.StringField(
        choices=['Heads', 'Tails'],
        widget=widgets.RadioSelect,
        label="Please make your choice."
    )
    partner_choice = models.StringField()
    pennypayoff = models.FloatField()

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        self.participant.vars['choice'] = self.choice
        if self.choice == 'Heads' and self.other_player().choice == 'Heads':
            if self.role == 'Column':
                self.pennypayoff = 0
            else:  # Row
                if self.subsession.stage == 1:
                    self.pennypayoff = 1
                elif self.subsession.stage == 2:
                    self.pennypayoff = 9
                else:
                    self.pennypayoff = 0.50
        else:
            payoff = {
                'Heads': {'Tails': [0, 1]},
                'Tails': {
                    'Tails': [1, 0],
                    'Heads': [0, 1]
                }
            }
            r = 0 if self.role == 'Row' else 1  # position of payoff in list
            self.pennypayoff = payoff[self.group.get_player_by_role('Row').choice][self.group.get_player_by_role('Column').choice][r]
            self.partner_choice = self.get_others_in_group()[0].choice


def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'role', 'my_choice', 'partner_choice', 'payoff']
    for p in players:
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.role, p.choice, p.get_others_in_group()[0].choice, p.pennypayoff]

