from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import math as M
import random as R

author = 'Corey Scheinfeld'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'participation'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'participation/instructions.html'


class Subsession(BaseSubsession):
    winner = models.StringField()
    bonus = models.IntegerField()
    def creating_session(self):
        alpha = []
        beta = []
        matrix = self.get_group_matrix()
        for i in range(len(matrix[0])):
            if(i < (M.ceil((len(matrix[0])+1)/2))):
                beta.append(i+1)
            else:
                alpha.append(i+1)
        new_matrix = [alpha, beta]
        self.set_group_matrix(new_matrix)

    def set_up(self):
        matrix = self.get_group_matrix()
        for p in matrix[0]:
            p.group_type = 'Alpha'
            p.personal_bonus = (R.randrange(0, 55))
        for p in matrix[1]:
            p.group_type = 'Beta'
            p.personal_bonus = (R.randrange(0, 55))

    def determine_winner(self):
        matrix = self.get_groups()

        if(matrix[0].total_participants > matrix[1].total_participants):
            matrix[0].bonus = 105
            matrix[1].bonus = 5
            winner = 'Alpha'
        if(matrix[0].total_participants < matrix[1].total_participants):
            matrix[0].bonus = 5
            matrix[1].bonus = 105
            winner = 'Beta'
        if(matrix[0].total_participants == matrix[1].total_participants):
            matrix[0].bonus = 55
            matrix[1].bonus = 55
            winner = 'Tie'

    def set_payoffs(self):
        players = self.get_players()
        for p in players:
            if p.group_type == 'Alpha':
                p.group_bonus = matrix[0].bonus
            else:
                p.group_bonus = matrix[1].bonus

            if p.choice == 'Do Not Participate':
                p.payoff = p.personal_bonus + p.group_bonus
            if p.choice == 'Participate':
                p.payoff = p.group_bonus


class Group(BaseGroup):
    total_participants = models.IntegerField()
    bonus = models.IntegerField()
    def set_participants(self):
        for i in self.get_players():
            if( i.choice == 'Participate'):
                self.total_participants += 1



class Player(BasePlayer):
    group_type = models.StringField()
    group_bonus = models.IntegerField()
    personal_bonus = models.IntegerField()
    choice = models.StringField(
    choices = ['Participate', 'Do Not Participate']
    )
