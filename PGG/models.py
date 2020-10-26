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
            num_players = 0
            rand_val = itertools.cycle(['pun_partisan', 'reg_partisan', 'pun_control', 'reg_control', 'pun_partisan', 'reg_partisan', 'pun_partisan', 'reg_partisan', 'pun_partisan', 'reg_partisan'])
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
    group_pot = models.FloatField(initial = 0)
    playerA = models.StringField()
    playerB = models.StringField()
    playerC = models.StringField()
    A_cont = models.FloatField()
    B_cont = models.FloatField()
    C_cont = models.FloatField()
    A_payoff = models.FloatField()
    B_payoff = models.FloatField()
    C_payoff = models.FloatField()
    A_punished = models.FloatField(initial = 0)
    B_punished = models.FloatField(initial = 0)
    C_punished = models.FloatField(initial = 0)
    def adjust_group(self):
        if self.subsession.round_number == 1:
            labels = ['A', 'B', 'C']
            val = 0
            for p in self.get_players():
                p.participant.vars['label'] = labels[val]
                val += 1
                p.participant.vars['party'] = p.affiliation
        for players in self.get_players():
            if (players.participant.vars['role'] != 'follower'):
                self.type = 'reg_partisan'
            if players.participant.vars['label'] == 'A':
                players.label = 'A'
                self.playerA =  players.participant.vars['party']
            if players.participant.vars['label'] == 'B':
                players.label = 'B'
                self.playerB = players.participant.vars['party']
            if players.participant.vars['label'] == 'C':
                players.label = 'C'
                self.playerC = players.participant.vars['party']
    def set_pot(self):
        for players in self.get_players():
            self.group_pot = self.group_pot + players.group_contribution
            players.kept = 20 - players.group_contribution
        for players in self.get_players():
            players.individual_share = round(self.group_pot*(2/3), 2)
            players.first_payoff = 20 - players.group_contribution + round(players.individual_share, 2)
        players = self.get_players()
        self.A_cont = players[0].group_contribution
        self.B_cont = players[1].group_contribution
        self.C_cont = players[2].group_contribution
        self.A_payoff = players[0].first_payoff
        self.B_payoff = players[1].first_payoff
        self.C_payoff = players[2].first_payoff
    def distribute_punishments(self):
        for player in self.get_players():
            if player.participant.vars['label'] == 'A':
                player.punishA = 0
                self.B_punished = self.B_punished + player.punishB
                self.C_punished = self.C_punished + player.punishC
            elif player.participant.vars['label'] == 'B':
                player.punishB = 0
                self.A_punished = self.A_punished + player.punishA
                self.C_punished = self.C_punished + player.punishC
            elif player.participant.vars['label'] == 'C':
                player.punishC = 0
                self.A_punished = self.A_punished + player.punishA
                self.B_punished = self.B_punished + player.punishB
        for player in self.get_players():
            if player.participant.vars['label'] == 'A':
                player.punished = self.A_punished*3
            elif player.participant.vars['label'] == 'B':
                player.punished = self.B_punished*3
            else:
                player.punished = self.C_punished*3
            player.reduce = player.punishA +player.punishB + player.punishC
            if(player.first_payoff - player.punished < 0):
                player.round_payoff = 0
            else:
                player.round_payoff = player.first_payoff - player.punished
            player.round_payoff = round(player.round_payoff - player.reduce, 2)
    def set_final_payoff(self):
        for player in self.get_players():
            if self.type == 'pun_control' or self.type == 'pun_partisan':
                for i in range(1, self.subsession.round_number + 1):
                    player.final_payoff = player.in_round(i).round_payoff + player.final_payoff
            else:
                for i in range(1, self.subsession.round_number + 1):
                    player.final_payoff = player.in_round(i).first_payoff + player.final_payoff



class Player(BasePlayer):
    first_payoff = models.FloatField(initial = 0)
    final_payoff = models.FloatField(initial = 0)
    punished = models.FloatField()
    round_payoff = models.FloatField(initial = 0)
    affiliation = models.StringField(label = "", choices = ['Democrat', 'Republican'], widget=widgets.RadioSelect)
    label = models.StringField()
    group_contribution = models.FloatField(label = "Your Contribution to the Group Project:", min = 0, max = 20)
    individual_share = models.FloatField()
    kept = models.FloatField()
    choice = models.StringField(
    choices = ['Participate', 'Do Not Participate'])
    punishA = models.FloatField(label = "", min = 0, max = 5)
    punishB = models.FloatField(label = "", min = 0, max = 5)
    punishC = models.FloatField(label = "", min = 0, max = 5)
    reduce = models.FloatField()
