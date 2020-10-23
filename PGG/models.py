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

    instructions_reg = 'PGG/instructions_reg.html'
    instructions_pun = 'PGG/instructions_pun.html'

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            num_players = 1
            rand_val = itertools.cycle(['pun_partisan', 'pun_partisan', 'pun_partisan', 'pun_partisan', 'reg_partisan', 'reg_partisan', 'reg_partisan', 'reg_partisan', 'pun_control', 'reg_control'])
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
    group_pot = models.IntegerField(initial = 0)
    playerA = models.StringField()
    playerB = models.StringField()
    playerC = models.StringField()
    A_cont = models.IntegerField()
    B_cont = models.IntegerField()
    C_cont = models.IntegerField()
    A_payoff = models.IntegerField()
    B_payoff = models.IntegerField()
    C_payoff = models.IntegerField()
    A_punished = models.IntegerField(initial = 0)
    B_punished = models.IntegerField(initial = 0)
    C_punished = models.IntegerField(initial = 0)
    def adjust_group(self):
        labels = ['A', 'B', 'C']
        val = 0
        for p in self.get_players():
            p.label = labels[val]
            val += 1
            if (p.participant.vars['role'] != 'follower'):
                self.type = p.participant.vars['role']
        players = self.get_players()
        self.playerA = players[0].affiliation
        self.playerB = players[1].affiliation
        self.playerC = players[2].affiliation
    def set_pot(self):
        for players in self.get_players():
            self.group_pot = self.group_pot + players.group_contribution
            players.kept = 20 - players.group_contribution
        for players in self.get_players():
            players.individual_share = int(self.group_pot*(2/3))
            players.payoff = 20 - players.group_contribution + players.individual_share
        players = self.get_players()
        self.A_cont = players[0].group_contribution
        self.B_cont = players[1].group_contribution
        self.C_payoff = players[2].group_contribution
        self.A_payoff = int(players[0].payoff)
        self.B_payoff = int(players[1].payoff)
        self.C_payoff = int(players[2].payoff)
    def distribute_punishments(self):
        for player in self.get_players():
            self.A_punished = self.A_punished + player.punishA
            self.B_punished = self.B_punished + player.punishB
            self.B_punished = self.B_punished + player.punishB
        for player in self.get_players():
            if player.label == 'A':
                player.punished = self.A_punished*3
            elif player.label == 'B':
                player.punished = self.B_punished*3
            else:
                player.punished = self.C_punished*3
            player.reduce = player.punishA +player.punishB + player.punishC
            if(player.payoff - player.punished < 0):
                player.round_payoff = 0
            else:
                player.round_payoff = int(player.payoff) - player.punished
            player.round_payoff = player.round_payoff - player.reduce
    def set_final_payoff(self):
        for player in self.get_players():
            if self.type == 'pun_control' or self.type == 'pun_partisan':
                for i in len(10):
                    player.final_payoff = player.in_round(i).round_payoff + player.final_payoff
            else:
                for i in len(10):
                    player.final_payoff = int(player.in_round(i).payoff) + player.final_payoff



class Player(BasePlayer):
    final_payoff = models.IntegerField(initial = 0)
    punished = models.IntegerField()
    round_payoff = models.IntegerField()
    affiliation = models.StringField(choices = ['Democrat', 'Republican'], widget=widgets.RadioSelect)
    label = models.StringField()
    group_contribution = models.IntegerField(label = "Your Contribution to the Group Project:", min = 0, max = 20)
    individual_share = models.IntegerField()
    kept = models.IntegerField()
    choice = models.StringField(
    choices = ['Participate', 'Do Not Participate'])
    punishA = models.IntegerField(initial = 0, min = 0, max = 5)
    punishB = models.IntegerField(initial = 0, min = 0, max = 5)
    punishC = models.IntegerField(initial = 0, min = 0, max = 5)
    reduce = models.IntegerField()