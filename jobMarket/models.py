from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
from random import choices

"""
Sim for Job Market Signaling game
"""


class Constants(BaseConstants):
    name_in_url = 'jobMarket'
    players_per_group = 2
    num_rounds = 3

    instructions_template = 'jobMarket/instructions.html'

    app_role = 'Applicant'
    emp_role = 'Employer'

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)
        new_matrix = []
        matrix = self.get_group_matrix()
        
        if(self.round_number == 2):
            for group in matrix:
                new_matrix.append([group[1], group[0]])       
            self.set_group_matrix(new_matrix)
            
        for group in self.get_groups():
            group.type = choices(['Slacker', 'Go-getter'], [0.6, 0.4])[0]
            print(group.type)

        

class Group(BaseGroup):
    type = models.StringField()


class Player(BasePlayer):
    choice = models.StringField(
        widget=widgets.RadioSelect)
    partner_choice = models.StringField()

    def choice_choices(self):
        if self.role == 'Applicant':
            return ['Easy Courses', 'Difficult Courses'] if self.round_number != 3 else [['Slacker', "I'm a Slacker."], ['Go-getter', "I'm a Go-getter."]]
        else:
            return ['Managerial Job', 'Clerical Job']

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        emp = self.group.get_player_by_role('Employer')
        app = self.group.get_player_by_role('Applicant')
        i = 0 if self.role == 'Employer' else 1

        if self.group.type == 'Slacker':
            if self.round_number != 3:
                payoff = {
                    'Managerial Job': {
                        'Easy Courses': [0, 100],
                        'Difficult Courses': [0, 50]
                    },
                    'Clerical Job': {
                        'Easy Courses': [60, 60],
                        'Difficult Courses': [60, 10]
                    }
                }
                self.payoff = payoff[emp.choice][app.choice][i]
            else:
                payoff = {
                    'Managerial Job': [0, 100],
                    'Clerical Job': [60, 60]
                }
                self.payoff = payoff[emp.choice][i]
        else:  # go-getter
            if self.round_number != 3:
                payoff = {
                    'Managerial Job': {
                        'Easy Courses': [100, 100],
                        'Difficult Courses': [100, 80]
                    },
                    'Clerical Job': {
                        'Easy Courses': [60, 60],
                        'Difficult Courses': [60, 40]
                    }
                }
                self.payoff = payoff[emp.choice][app.choice][i]
            else:
                payoff = {
                    'Managerial Job': [100, 100],
                    'Clerical Job': [60, 60]
                }
                self.payoff = payoff[emp.choice][i]
        self.partner_choice = self.get_others_in_group()[0].choice

def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'role', 'my_choice', 'partner_choice' 'payoff']
    for p in players:
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.role, p.choice, p.get_others_in_group()[0].choice, p.payoff]

