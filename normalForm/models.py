from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
from random import choice
"""
Sim for Repeated Normal Form game
"""


class Constants(BaseConstants):
    name_in_url = 'normalForm'
    players_per_group = 2
    num_rounds = 100

    instructions_template = 'normalForm/instructions.html'
    role = choice([1, 2])


class Subsession(BaseSubsession):
    end_round = models.BooleanField()

    def creating_session(self):
        self.end_round = True if self.round_number == self.session.config['number_of_rounds'] else False


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    opponent_next_move_belief = models.StringField()
    choice = models.StringField(widget=widgets.RadioSelect, label='Please make your choice.')

    def choice_choices(self):
        return ['One', 'Two'] if self.role() == 'Row' else ['Aay', 'Bee']

    def role(self):
        return 'Row' if self.id_in_group == Constants.role else 'Column'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff = {
            'One': {
                'Aay': [6, 2],
                'Bee': [3, 5]
            },
            'Two': {
                'Aay': [3, 5],
                'Bee': [5, 3]
            }
        }
        i = 0 if self.role() == 'Row' else 1
        self.payoff = payoff[self.group.get_player_by_role('Row').choice][self.group.get_player_by_role('Column').choice][i]

    def vars_for_template(self):
        if self.session.config['display_all_history']:
            if self.choice is None:  # for main page
                me_all = [p for p in self.in_previous_rounds()]
                other_all = [p for p in self.other_player().in_previous_rounds()]
                return {
                    'other': self.other_player(),
                    'players': zip(me_all, other_all)
                }
            else:  # for results page
                me_all = [p for p in self.in_all_rounds()]
                other_all = [p for p in self.other_player().in_all_rounds()]
                return {
                    'other': self.other_player(),
                    'players': zip(me_all, other_all)
                }
        else:
            if self.round_number == 1:
                return {
                    'other': self.other_player()
                }
            else:
                return {
                    'p1_last': self.in_round(self.round_number - 1),
                    'p2_last': self.other_player().in_round(self.round_number - 1),
                    'other': self.other_player()
                }

def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'role', 'my_choice', 'belief of opponents next move', 'partner_choice', 'payoff']
    for p in players:
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.role(), p.choice, p.opponent_next_move_belief, p.get_others_in_group()[0].choice, p.payoff]

