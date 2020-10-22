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

import math as M
import random as R
import itertools


author = 'Corey Scheinfeld'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'PGG'
    players_per_group = 3
    num_rounds = 10


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            num_players = 1
            rand_val = itertools.cycle(['pun-partisan', 'pun-partisan', 'pun-partisan', 'pun-partisan', 'reg_partisan', 'reg_partisan', 'reg_partisan', 'reg_partisan', 'pun_control', 'reg_control'])
            for p in self.get_players():
                if(num_players%3 == 0):
                    p.participant.vars['role'] = next(rand_val)
                else:
                    p.participant.vars['role'] = 'follower'
                num_players += 1
    def group_by_arrival_time_method(self, waiting_players):
        leaders = [p for p in waiting_players if p.participant.vars['role'] != 'follower']
        followers = [p for p in waiting_players if p.participant.vars['role'] == 'follower']

        if len(leaders) >= 1 and len(followers) >= 2:
            return [leaders[0], followers[0], followers[1]]


class Group(BaseGroup):
    type = models.StringField()
    playerA = models.StringField()
    playerB = models.StringField()
    playerC = models.StringField()
    rand_val = models.IntegerField()
    def adjust_group(self):
        labels = ['A', 'B', 'C']
        val = 0
        for p in self.get_players():
            p.label = labels[val]
            val += 1
            if (p.participant.vars['role'] != 'follower'):
                self.type = p.participant.vars['role']
        players = self.get_players()
        playerA = players[0].affiliation
        playerB = players[1].affiliation
        playerC = players[2].affiliation



class Player(BasePlayer):
    affiliation = models.StringField(widget=widgets.RadioSelect, choices = ['Democrat', 'Republican'])
    label = models.StringField()
    group_type = models.StringField()
    group_bonus = models.IntegerField()
    personal_bonus = models.IntegerField()
    choice = models.StringField(
    choices = ['Participate', 'Do Not Participate'])
