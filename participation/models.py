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
            get_player_by_id(p).group_type = 'Beta'
            get_player_by_id(p).bonus = (R.randrange(0, 55))
        for p in matrix[1]:
            get_player_by_id(p).group_type = 'ALpha'
            get_player_by_id(p).bonus = (R.randrange(0, 55))
    def set_payoffs(self):
        matrix = self.get_group_matrix()
        for i in len(matrix[0]):
            if( get_player_by_id(i).choice == 'Participate'):
                matrix[0].total_participants += 1
        for i in len(matrix[1]):
            if( get_player_by_id(i).choice == 'Participate'):
                matrix[1].total_participants += 1
        if(matrix[0].total_participants > matrix[1].total_participants):
            matrix[0].total = 105
            matrix[1].total = 5
            winner = 'Beta'
        if(matrix[0].total_participants < matrix[1].total_participants):
            matrix[0].total = 5
            matrix[1].total = 105
            winner = 'Alpha'
        if(matrix[0].total_participants == matrix[1].total_participants):
            matrix[0].total = 55
            matrix[1].total = 55
            winner = 'Tie'

        for p in matrix[0]:
            if get_player_by_id(p).choice == 'Do Not Participate':
                get_player_by_id(p).payoff = get_player_by_id(p).bonus + matrix[0].total
            if get_player_by_id(p).choice == 'Participate':
                get_player_by_id(p).payoff = matrix[0].total
        for p in matrix[2]:
            if get_player_by_id(p).choice == 'Do Not Participate':
                get_player_by_id(p).payoff = get_player_by_id(p).bonus + matrix[1].total
            if get_player_by_id(p).choice == 'Participate':
                get_player_by_id(p).payoff = matrix[1].total


class Group(BaseGroup):
    total_participants = models.IntegerField()
    total = models.IntegerField()




class Player(BasePlayer):
    group_type = models.StringField()
    bonus = models.IntegerField()
    choice = models.StringField(
    choices = ['Participate', 'Do Not Participate']
    )
