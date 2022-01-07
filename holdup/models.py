from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random

author = 'Corey Scheinfeld'

doc = """
Hold-up with Vengeance
"""


class Constants(BaseConstants):
    name_in_url = 'holdup'
    players_per_group = 2
    num_rounds = 5
    instructions_template = 'holdup/instructions.html'
    p1_role = 'Player 1'
    p2_role = 'Player 2'
    

class Subsession(BaseSubsession):
    def creating_session(subsession): 
        subsession.group_randomly(fixed_id_in_group=True)



class Group(BaseGroup):
    pass

class Player(BasePlayer):
    def other_player(self):
        return self.get_others_in_group()[0]
    
    decision = models.StringField(widget=widgets.RadioSelect,
                                  initial='',
                                  label="Please make your choice.")
    decision2 = models.StringField(widget=widgets.RadioSelect,
                                  initial='',
                                  label="Please make your choice.", 
                                  choices = ['Accept', 'Reject'])

    def decision_choices(self):
        if self.role == 'Player 1':
            return ['In', 'Out']
        else:
            return ['Renege', 'Honor']

    def set_payoff(self):
        p1 = self.group.get_player_by_role('Player 1')
        p2 = self.group.get_player_by_role('Player 2')
        roleNum = None
        if self.role == 'Player 1':
            roleNum = 0
        else:
            roleNum = 1
        payoff = {
            'In': {
                    'Honor': {
                        '': [5, 5]
                    },
                    'Renege': {
                        'Accept': [1, 9],
                        'Reject': [0, 2]
                    }
                },
            'Out': {
                    '': {
                        '': [2, 2]
                    },
                }
        }
        self.payoff = payoff[p1.decision][p2.decision][p1.decision2][roleNum]


def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'role', 'player1_decision1', 'player2_decision', 'player1_decision2', 'payoff']
    for p in players:
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.role, p.group.get_player_by_role('Player 1').decision, p.group.get_player_by_role('Player 2').decision, p.group.get_player_by_role('Player 1').decision2, p.payoff]


