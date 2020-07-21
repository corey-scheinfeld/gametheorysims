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


class Subsession(BaseSubsession):

    bonus = models.IntegerField()
    def creating_session(self):
        alpha = []
        beta = []
        matrix = self.get_group_matrix()
        for i in len(matrix):
            if(i < (M.ceil((len(matrix)+1)/2))):
                beta.append(matrix(i))
            else:
                alpha.append(matrix(i))
        new_matrix = [alpha, beta]
        self.set_group_matrix(new_matrix)
    def set_up(self):
        matrix_len = len(s.get_group_matrix())
        for p in players:
            if p.id_in_subsession < (M.ceil((len(matrix)+1)/2)):
                p.group_type = 'Beta'
            else:
                p.group_type = 'Alpha'
            p.bonus = (R.randrange(0, 55))



class Group(BaseGroup):
    total_participants = models.IntegerField()


class Player(BasePlayer):
    group_type = models.StringField()
    bonus = models.IntegerField()

    choice = models.StringField(
    choices = ['Participate', 'Do Not Participate']
    )
