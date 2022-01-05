from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
import random

"""
Sim for 'Non-credible Threat Game'
"""


class Constants(BaseConstants):
    name_in_url = 'nct'
    players_per_group = 2
    num_rounds = 2

    instructions_template = 'nct/instructions.html'
    instructions_template2 = 'nct/instructions2.html'

    role = random.choice([1, 2])


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(widget=widgets.RadioSelect,
                                  initial='',
                                  label="Please make your choice.")

    def decision_choices(self):
        if self.role() == 1:
            if self.round_number == 1:
                return ['In', 'Out']
            else:
                return ['Up', 'Down']
        else:
            if self.round_number == 1:
                return ['Up', 'Down']
            else:
                return ['A', 'B']

    def role(self):
        if self.id_in_group == Constants.role:
            if(self.round_number == 1):
                return 1
            else:
                return 2       
        else:
            if(self.round_number == 1):
                return 2
            else:
                return 1

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        p1 = self.group.get_player_by_role(1)
        p2 = self.group.get_player_by_role(2)
        if self.round_number == 1:
            payoff = {
                'In': {
                        'Up': [500, 100],
                        'Down': [-1000, -1000]
                    },
                'Out': {
                        '': [100, 600]
                    }
            }
            self.payoff = payoff[p1.decision][p2.decision][self.role() - 1]
        else:
            payoff = {
                'Up': {
                    'A': [50, 100],
                    'B': [-50, -50]
                },
                'Down': {
                    'A': [100, 50],
                    'B': [0, -100]
                }
            }
            self.payoff = payoff[p1.decision][p2.decision][self.role() - 1]

def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'role', 'my_choice', 'partner_choice' 'payoff']
    for p in players:
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.role(), p.decision, p.get_others_in_group()[0].decision, p.payoff]

