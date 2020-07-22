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
    num_rounds = 10

    instructions_template = 'participation/instructions.html'
    instructions_template2 = 'participation/part2.html'



class Subsession(BaseSubsession):
    winner = models.StringField()
    alpha = models.IntegerField()
    beta = models.IntegerField()
    def creating_session(self):
        if self.round_number == 1:
            alpha_group = []
            beta_group = []
            matrix = self.get_group_matrix()
            for i in range(len(matrix[0])):
                if(i < (M.ceil((len(matrix[0])+1)/2))):
                    beta_group.append(i+1)
                else:
                    alpha_group.append(i+1)
            self.alpha = len(alpha_group)
            self.beta = len(beta_group)
            new_matrix = [alpha_group, beta_group]
            self.set_group_matrix(new_matrix)

        elif (self.round_number > 1 and self.round_number < 6):
            self.group_like_round(1)

        if self.round_number == 6:
            all_players = self.get_players()
            alpha_group = []
            beta_group = []
            R.shuffle(all_players)
            for i in range(len(all_players)):
                if(i < (M.ceil((len(all_players)*2)/3))):
                    beta_group.append(i+1)
                else:
                    alpha_group.append(i+1)
            self.alpha = len(alpha_group)
            self.beta = len(beta_group)
            new_matrix = [alpha_group, beta_group]
            self.set_group_matrix(new_matrix)

        elif (self.round_number > 6 and self.round_number < 10):
            self.group_like_round(6)


    def set_up(self):
        matrix = self.get_group_matrix()
        for p in matrix[0]:
            p.group_type = 'Alpha'
            p.personal_bonus = (R.randrange(0, 55))
        for p in matrix[1]:
            p.group_type = 'Beta'
            p.personal_bonus = (R.randrange(0, 55))

    def set_payoffs(self):
        matrix = self.get_groups()
        group1 = 0
        group2 = 0
        for i in matrix[0].get_players():
            if( i.choice == 'Participate'):
                group1 = group1 + 1
        for i in matrix[1].get_players():
            if( i.choice == 'Participate'):
                group2 = group2 + 1
        if(group1 > group2):
            matrix[0].bonus = 105
            matrix[1].bonus = 5
            self.winner = 'Alpha'
        if(group1 < group2):
            matrix[0].bonus = 5
            matrix[1].bonus = 105
            self.winner = 'Beta'
        if(group1 == group2):
            matrix[0].bonus = 55
            matrix[1].bonus = 55
            self.winner = 'Tie'

        for p in matrix[0].get_players():
            p.group_bonus = matrix[0].bonus
        for p in matrix[1].get_players():
            p.group_bonus = matrix[1].bonus
        for p in self.get_players():
            if p.choice == 'Do Not Participate':
                p.payoff = p.personal_bonus + p.group_bonus
            if p.choice == 'Participate':
                p.payoff = p.group_bonus


class Group(BaseGroup):
    total_participants = models.IntegerField()
    bonus = models.IntegerField()





class Player(BasePlayer):
    group_type = models.StringField()
    group_bonus = models.IntegerField()
    personal_bonus = models.IntegerField()
    choice = models.StringField(
    choices = ['Participate', 'Do Not Participate']
    )
