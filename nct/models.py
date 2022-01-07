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

    p1_role = 'Player 1'
    p2_role = 'Player 2'


class Subsession(BaseSubsession):
     def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)

        new_matrix = []
        matrix = self.get_group_matrix()
        
        if(self.round_number == 2):
            for group in matrix:
                new_matrix.append([group[1], group[0]])   
            self.set_group_matrix(new_matrix)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(widget=widgets.RadioSelect,
                                  initial='',
                                  label="Please make your choice.")
    partner_decision = models.StringField()

    def decision_choices(self):
        if self.role == 'Player 1':
            if self.round_number == 1:
                return ['In', 'Out']
            else:
                return ['Up', 'Down']
        else:
            if self.round_number == 1:
                return ['Up', 'Down']
            else:
                return ['A', 'B']

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        p1 = self.group.get_player_by_role('Player 1')
        p2 = self.group.get_player_by_role('Player 2')
        index = 0 if self.role == 'Player 1' else 1
        if self.round_number == 1:
            print(p2.decision)
            payoff = {
                'In': {
                        'Up': [500, 100],
                        'Down': [-1000, -1000]
                    },
                'Out': {
                        '': [100, 600],
                    }
            }
            self.payoff = payoff[p1.decision][p2.decision][index]
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
            self.payoff = payoff[p1.decision][p2.decision][index]
        self.partner_decision = p.get_others_in_group()[0].decision

def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'role', 'my_choice', 'partner_choice' 'payoff']
    for p in players:
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.role, p.decision, p.get_others_in_group()[0].decision, p.payoff]

