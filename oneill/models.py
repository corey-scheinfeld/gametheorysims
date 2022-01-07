from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
import random

"""
Sim for O'Neill game.
"""


class Constants(BaseConstants):
    name_in_url = 'oneill'
    players_per_group = 2
    num_rounds = 5

    instructions_template = 'oneill/instructions.html'
    row_role = 'Row'
    col_role = 'Column'


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
        else:
            self.group_like_round(1)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.StringField(
        choices=['Joker', 'Ace', 'Two', 'Three'],
        widget=widgets.RadioSelect,
        label="Please choose your card.")
    partner_choice = models.StringField()

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.role == 'Row':
            payoff = {
                'Joker':
                    {
                        'Joker': 5,
                        'Ace': -5,
                        'Two': -5,
                        'Three': -5
                    },
                'Ace':
                    {
                        'Joker': -5,
                        'Ace': -5,
                        'Two': 5,
                        'Three': 5
                    },
                'Two':
                    {
                        'Joker': -5,
                        'Ace': 5,
                        'Two': -5,
                        'Three': 5
                    },
                'Three':
                    {
                        'Joker': -5,
                        'Ace': 5,
                        'Two': 5,
                        'Three': -5
                    }
            }
            self.payoff = payoff[self.choice][self.other_player().choice]
        else:
            payoff = {
                'Joker':
                    {
                        'Joker': -5,
                        'Ace': 5,
                        'Two': 5,
                        'Three': 5
                    },
                'Ace':
                    {
                        'Joker': 5,
                        'Ace': 5,
                        'Two': -5,
                        'Three': -5
                    },
                'Two':
                    {
                        'Joker': 5,
                        'Ace': -5,
                        'Two': 5,
                        'Three': -5
                    },
                'Three':
                    {
                        'Joker': 5,
                        'Ace': -5,
                        'Two': -5,
                        'Three': 5
                    }
            }
            self.payoff = payoff[self.choice][self.other_player().choice]
            self.partner_choice = self.other_player().choice

def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'role', 'my_choice', 'partner_choice', 'payoff']
    for p in players:
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.role, p.choice, p.get_others_in_group()[0].choice, p.payoff]


